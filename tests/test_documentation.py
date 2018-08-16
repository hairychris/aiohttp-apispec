import json
from yarl import URL


def test_app_swagger_url(aiohttp_app):
    urls = [route.url_for() for route in aiohttp_app.app.router.routes()]
    assert URL('/v1/api/docs/api-docs') in urls


async def test_app_swagger_json(aiohttp_app):
    resp = await aiohttp_app.get('/v1/api/docs/api-docs')
    docs = await resp.json()
    assert docs['info']['title'] == 'My Documentation'
    assert docs['info']['version'] == 'v1'
    docs['paths']['/v1/test']['get']['parameters'] = sorted(
        docs['paths']['/v1/test']['get']['parameters'], key=lambda x: x['name']
    )
    assert json.dumps(docs['paths']['/v1/test']['get'], sort_keys=True) == json.dumps(
        {
            'parameters': [
                {
                    'in': 'query',
                    'name': 'bool_field',
                    'required': False,
                    'type': 'boolean',
                },
                {
                    'format': 'int32',
                    'in': 'query',
                    'name': 'id',
                    'required': False,
                    'type': 'integer',
                },
                {
                    'collectionFormat': 'multi',
                    'in': 'query',
                    'items': {'format': 'int32', 'type': 'integer'},
                    'name': 'list_field',
                    'required': False,
                    'type': 'array',
                },
                {
                    'description': 'name',
                    'in': 'query',
                    'name': 'name',
                    'required': False,
                    'type': 'string',
                },
            ],
            'responses': {},
            'tags': ['mytag'],
            'summary': 'Test method summary',
            'description': 'Test method description',
            'produces': ['application/json'],
        },
        sort_keys=True,
    )
    docs['paths']['/v1/class_echo']['get']['parameters'] = sorted(
        docs['paths']['/v1/class_echo']['get']['parameters'], key=lambda x: x['name']
    )
    assert json.dumps(
        docs['paths']['/v1/class_echo']['get'], sort_keys=True
    ) == json.dumps(
        {
            'parameters': [
                {
                    'in': 'query',
                    'name': 'bool_field',
                    'required': False,
                    'type': 'boolean',
                },
                {
                    'format': 'int32',
                    'in': 'query',
                    'name': 'id',
                    'required': False,
                    'type': 'integer',
                },
                {
                    'collectionFormat': 'multi',
                    'in': 'query',
                    'items': {'format': 'int32', 'type': 'integer'},
                    'name': 'list_field',
                    'required': False,
                    'type': 'array',
                },
                {
                    'description': 'name',
                    'in': 'query',
                    'name': 'name',
                    'required': False,
                    'type': 'string',
                },
            ],
            'responses': {},
            'tags': ['mytag'],
            'summary': 'View method summary',
            'description': 'View method description',
            'produces': ['application/json'],
        },
        sort_keys=True,
    )
