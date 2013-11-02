# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Contest'
        db.create_table(u'contest_contest', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('tinymce.models.HTMLField')()),
            ('end', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'contest', ['Contest'])

        # Adding model 'Group'
        db.create_table(u'contest_group', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('capacity', self.gf('django.db.models.fields.IntegerField')()),
            ('contest', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contest.Contest'])),
        ))
        db.send_create_signal(u'contest', ['Group'])

        # Adding model 'Contestant'
        db.create_table(u'contest_contestant', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('surname', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('sponsor', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contest.Group'])),
        ))
        db.send_create_signal(u'contest', ['Contestant'])


    def backwards(self, orm):
        # Deleting model 'Contest'
        db.delete_table(u'contest_contest')

        # Deleting model 'Group'
        db.delete_table(u'contest_group')

        # Deleting model 'Contestant'
        db.delete_table(u'contest_contestant')


    models = {
        u'contest.contest': {
            'Meta': {'object_name': 'Contest'},
            'description': ('tinymce.models.HTMLField', [], {}),
            'end': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'contest.contestant': {
            'Meta': {'object_name': 'Contestant'},
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