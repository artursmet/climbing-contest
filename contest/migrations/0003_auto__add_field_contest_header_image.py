# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Contest.header_image'
        db.add_column(u'contest_contest', 'header_image',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Contest.header_image'
        db.delete_column(u'contest_contest', 'header_image')


    models = {
        u'contest.contest': {
            'Meta': {'object_name': 'Contest'},
            'description': ('tinymce.models.HTMLField', [], {}),
            'end': ('django.db.models.fields.DateTimeField', [], {}),
            'header_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'contest.contestant': {
            'Meta': {'object_name': 'Contestant'},
            'age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contest.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sponsor': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        u'contest.group': {
            'Meta': {'object_name': 'Group'},
            'capacity': ('django.db.models.fields.IntegerField', [], {}),
            'contest': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contest.Contest']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['contest']