import json

from hfexcel import HFExcel

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from django.views.generic.base import TemplateResponseMixin

from .forms import DocumentUploadForm


class DocumentManagerView(TemplateResponseMixin, View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        form = DocumentUploadForm()
        context = {
            'form': form,
        }
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        version = '0.0.6'
        form = DocumentUploadForm(data=request.POST)

        if form.is_valid():
            data = form.cleaned_data.get('data')
            excel_data = json.loads(data)
            hf_workbook = HFExcel.hf_workbook()
            hf_workbook.filter().populate_with_json(excel_data)
            hf_workbook.save()
            if hf_workbook.output:
                web_data = hf_workbook.output.getvalue()
                response = HttpResponse(content_type='application/vnd.ms-excel')
                response.write(web_data)
                response['Content-Disposition'] = f"attachment; filename=hfexcel-v{version}.xlsx"
                return response

        context = {
            'data': self.data,
            'form': form,
        }
        return self.render_to_response(context)
