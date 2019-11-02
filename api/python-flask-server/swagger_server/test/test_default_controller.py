# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.likes import Likes  # noqa: E501
from swagger_server.models.pickup_lines import PickupLines  # noqa: E501
from swagger_server.models.profiles import Profiles  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_createlikes(self):
        """Test case for createlikes

        Create a likes
        """
        body = Likes()
        response = self.client.open(
            '/likes',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_createpickup_lines(self):
        """Test case for createpickup_lines

        Create a pickup_lines
        """
        body = PickupLines()
        response = self.client.open(
            '/pickup_lines',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_createprofiles(self):
        """Test case for createprofiles

        Create a profiles
        """
        body = Profiles()
        response = self.client.open(
            '/profiles',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_deletelikes(self):
        """Test case for deletelikes

        Delete a likes
        """
        response = self.client.open(
            '/likes/{likesId}'.format(likesId='likesId_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_deletepickup_lines(self):
        """Test case for deletepickup_lines

        Delete a pickup_lines
        """
        response = self.client.open(
            '/pickup_lines/{pickup_linesId}'.format(pickup_linesId='pickup_linesId_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_deleteprofiles(self):
        """Test case for deleteprofiles

        Delete a profiles
        """
        response = self.client.open(
            '/profiles/{profilesId}'.format(profilesId='profilesId_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_getalllikes(self):
        """Test case for getalllikes

        List All likes
        """
        response = self.client.open(
            '/likes',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_getallpickup_lines(self):
        """Test case for getallpickup_lines

        List All pickup_lines
        """
        response = self.client.open(
            '/pickup_lines',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_getallprofiles(self):
        """Test case for getallprofiles

        List All profiles
        """
        response = self.client.open(
            '/profiles',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_getlikes(self):
        """Test case for getlikes

        Get a likes
        """
        response = self.client.open(
            '/likes/{likesId}'.format(likesId='likesId_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_getpickup_lines(self):
        """Test case for getpickup_lines

        Get a pickup_lines
        """
        response = self.client.open(
            '/pickup_lines/{pickup_linesId}'.format(pickup_linesId='pickup_linesId_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_getprofiles(self):
        """Test case for getprofiles

        Get a profiles
        """
        response = self.client.open(
            '/profiles/{profilesId}'.format(profilesId='profilesId_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_updatelikes(self):
        """Test case for updatelikes

        Update a likes
        """
        body = Likes()
        response = self.client.open(
            '/likes/{likesId}'.format(likesId='likesId_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_updatepickup_lines(self):
        """Test case for updatepickup_lines

        Update a pickup_lines
        """
        body = PickupLines()
        response = self.client.open(
            '/pickup_lines/{pickup_linesId}'.format(pickup_linesId='pickup_linesId_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_updateprofiles(self):
        """Test case for updateprofiles

        Update a profiles
        """
        body = Profiles()
        response = self.client.open(
            '/profiles/{profilesId}'.format(profilesId='profilesId_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
