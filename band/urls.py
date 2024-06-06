from django.urls import path
from band.views.get import GetBandSpecific
from band.views.create import CreateBand, CreateBandMember
from band.views.edit import EditBand
from band.views.delete import DeleteBand
from band.views.recover import RecoverBand
from band.views.get import GetBand
from band.views.get import GetBandMemberList
from band.views.enable import EnableBand
from band.views.disable import DisableBand
from band.views.remove import RemoveBandMember


urlpatterns = [
    path('band/get/', GetBand.as_view(), name="get_band"),
    path('band/get/<int:bandid>/', GetBandSpecific.as_view(), name="get_band_specific"),
    path('band/post/', CreateBand.as_view(), name="post_band"),
    path('band/edit/<int:bandid>/', EditBand.as_view(), name="edit_band"),
    path('band/delete/<int:bandid>/', DeleteBand.as_view(), name="delete_band"),
    path('band/recover/<int:bandid>/', RecoverBand.as_view(), name="recover_band"),
    path('band/get/member/<int:bandid>/', GetBandMemberList.as_view(), name="get_band_member"),
    path('band/disable/<int:bandid>/', DisableBand.as_view(), name="disable_band"),
    path('band/enable/<int:bandid>/', EnableBand.as_view(), name="enable_band"),
    path('band/add/member/', CreateBandMember.as_view(), name="add_band_member"),
    path('band/remove/member/<int:bandid>/', RemoveBandMember.as_view(), name="remove_band_member")
]