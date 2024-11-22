from .extensions import db
from datetime import datetime

class IncidentVideo(db.Model):
    __tablename__ = 'incident_videos'

    id = db.Column(db.Integer, primary_key=True)
    video_url = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    report_id = db.Column(db.Integer, db.ForeignKey('incident_reports.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'video_url': self.video_url,
            'created_at': self.created_at.isoformat(),
            'report_id': self.report_id
        }