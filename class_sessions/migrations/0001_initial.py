# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ClassSession'
        db.create_table(u'class_sessions_classsession', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('session_start', self.gf('django.db.models.fields.DateTimeField')()),
            ('session_end', self.gf('django.db.models.fields.DateTimeField')()),
            ('class_type', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('teacher', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['teachers.TeacherProfile'])),
            ('fee', self.gf('django.db.models.fields.FloatField')()),
            ('session_id', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'class_sessions', ['ClassSession'])

        # Adding M2M table for field students on 'ClassSession'
        m2m_table_name = db.shorten_name(u'class_sessions_classsession_students')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('classsession', models.ForeignKey(orm[u'class_sessions.classsession'], null=False)),
            ('userprofile', models.ForeignKey(orm[u'core.userprofile'], null=False))
        ))
        db.create_unique(m2m_table_name, ['classsession_id', 'userprofile_id'])

        # Adding M2M table for field files on 'ClassSession'
        m2m_table_name = db.shorten_name(u'class_sessions_classsession_files')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('classsession', models.ForeignKey(orm[u'class_sessions.classsession'], null=False)),
            ('teacherfile', models.ForeignKey(orm[u'teachers.teacherfile'], null=False))
        ))
        db.create_unique(m2m_table_name, ['classsession_id', 'teacherfile_id'])


    def backwards(self, orm):
        # Deleting model 'ClassSession'
        db.delete_table(u'class_sessions_classsession')

        # Removing M2M table for field students on 'ClassSession'
        db.delete_table(db.shorten_name(u'class_sessions_classsession_students'))

        # Removing M2M table for field files on 'ClassSession'
        db.delete_table(db.shorten_name(u'class_sessions_classsession_files'))


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'class_sessions.classsession': {
            'Meta': {'object_name': 'ClassSession'},
            'class_type': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'fee': ('django.db.models.fields.FloatField', [], {}),
            'files': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['teachers.TeacherFile']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'session_end': ('django.db.models.fields.DateTimeField', [], {}),
            'session_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'session_start': ('django.db.models.fields.DateTimeField', [], {}),
            'students': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.UserProfile']", 'symmetrical': 'False'}),
            'teacher': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['teachers.TeacherProfile']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'core.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'about': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'teachers.teacherfile': {
            'Meta': {'object_name': 'TeacherFile'},
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'teachers.teacherprofile': {
            'Meta': {'object_name': 'TeacherProfile'},
            'about': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'audio_sample': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'availability': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'profile_picture': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'profile_video': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['class_sessions']