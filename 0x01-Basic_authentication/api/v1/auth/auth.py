#!/usr/bin/env python3
""" API Authentication
"""
from flask import request
from typing import List, TypeVar

class Auth():
    """ Manages API authetication"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """For autorization check"""
        if path is None or excluded_paths is None or not len(excluded_paths):
            return True
        if path[-1] != '/':
            path += '/'
        for p in excluded_paths:
            if p.endswith('*'):
                if path.startswith(p[:1]):
                    return False
        return False if path in excluded_paths else True
        
    def authorization_header(self, request=None) -> str:
        """ Authorization header check """
        if request:
            return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """ Current User Method """
        return None

