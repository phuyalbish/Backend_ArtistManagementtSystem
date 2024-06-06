from rest_framework import serializers, viewsets
from band.models import Band,BandMember


class BandMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = BandMember
        fields = ['id', 'band', 'artist']



class BandSerializer(serializers.ModelSerializer):
    members = BandMemberSerializer(many=True, read_only=True)
    class Meta:
        model = Band
        fields = ['id', 'bandname', 'name', 'is_deleted', 'is_disabled', 'profile_img', 'banner_img', 'modified_by', 'members']
    


