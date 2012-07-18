# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SharedSite'
        db.create_table('sharedUrl_sharedsite', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('ip', self.gf('django.db.models.fields.IPAddressField')(max_length=15)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('user', self.gf('django.db.models.fields.SlugField')(max_length=50)),
        ))
        db.send_create_signal('sharedUrl', ['SharedSite'])


    def backwards(self, orm):
        # Deleting model 'SharedSite'
        db.delete_table('sharedUrl_sharedsite')


    models = {
        'sharedUrl.sharedsite': {
            'Meta': {'object_name': 'SharedSite'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'user': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['sharedUrl']