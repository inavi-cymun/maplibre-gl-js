### Main
- [Map](https://maplibre.org/maplibre-gl-js/docs/API/classes/maplibregl.Map/)

```js
const map = new maplibregl.Map({
    container: 'map',
    style: 'https://demotiles.maplibre.org/style.json', // style URL
    center: [-123.068053,44.056453], // starting position [lng, lat]
    zoom: 1, // starting zoom
});
```

### Markers and Controls
- [AttributionControl](https://maplibre.org/maplibre-gl-js/docs/API/classes/maplibregl.AttributionControl/)
- [FullscreenControl](https://maplibre.org/maplibre-gl-js/docs/API/classes/maplibregl.FullscreenControl/)
- [GeolocateControl](https://maplibre.org/maplibre-gl-js/docs/API/classes/maplibregl.GeolocateControl/)
- [Hash](https://maplibre.org/maplibre-gl-js/docs/API/classes/maplibregl.Hash/)
- [LogoControl](https://maplibre.org/maplibre-gl-js/docs/API/classes/maplibregl.LogoControl/)
- [NavigationControl](https://maplibre.org/maplibre-gl-js/docs/API/classes/maplibregl.NavigationControl/)
- [ScaleControl](https://maplibre.org/maplibre-gl-js/docs/API/classes/maplibregl.ScaleControl/)
- [TerrainControl](https://maplibre.org/maplibre-gl-js/docs/API/classes/maplibregl.TerrainControl/)
- [Marker](https://maplibre.org/maplibre-gl-js/docs/API/classes/maplibregl.Marker/)
- [Popup](https://maplibre.org/maplibre-gl-js/docs/API/classes/maplibregl.Popup/)
  
```js
//Add Control
map.addControl(new maplibregl.GeolocateControl({
    positionOptions: {
        enableHighAccuracy: true
    },
    trackUserLocation: true
}));
map.addControl(new maplibregl.FullscreenControl({container: document.querySelector('body')}));


//Add Marker
let marker = new maplibregl.Marker({
    color: "#FFFFFF",
    draggable: true
  }).setLngLat([30.5, 50.5])
  .addTo(map);

//Add Popup
let markerHeight = 50, markerRadius = 10, linearOffset = 25;
let popupOffsets = {
 'top': [0, 0],
 'top-left': [0,0],
 'top-right': [0,0],
 'bottom': [0, -markerHeight],
 'bottom-left': [linearOffset, (markerHeight - markerRadius + linearOffset) * -1],
 'bottom-right': [-linearOffset, (markerHeight - markerRadius + linearOffset) * -1],
 'left': [markerRadius, (markerHeight - markerRadius) * -1],
 'right': [-markerRadius, (markerHeight - markerRadius) * -1]
 };
let popup = new maplibregl.Popup({offset: popupOffsets, className: 'my-class'})
  .setLngLat(e.lngLat)
  .setHTML("<h1>Hello World!</h1>")
  .setMaxWidth("300px")
  .addTo(map);

```

### Geography and Geometry
- [EdgeInsets](https://maplibre.org/maplibre-gl-js/docs/API/classes/maplibregl.EdgeInsets/)
- [LngLat](https://maplibre.org/maplibre-gl-js/docs/API/classes/maplibregl.LngLat/)
- [LngLatBounds](https://maplibre.org/maplibre-gl-js/docs/API/classes/maplibregl.LngLatBounds/)
- [MercatorCoordinate](https://maplibre.org/maplibre-gl-js/docs/API/classes/maplibregl.MercatorCoordinate/)
- [LngLatBoundsLike](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.LngLatBoundsLike/)
- [LngLatLike](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.LngLatLike/)
- [PaddingOptions](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.PaddingOptions/)
- [PointLike](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.PointLike/)
```js
//EdgeInsets {top: 0, bottom: 0, left: 0, right: 0}
let edgeinsets = map.transform._edgeInsets;

//Add LngLat , LngLatBounds
let sw = new maplibregl.LngLat(-73.9876, 40.7661);
let ne = new maplibregl.LngLat(-73.9397, 40.8002);
let llb = new maplibregl.LngLatBounds(sw, ne);

//Add MercatorCoordinate
let nullIsland = new maplibregl.MercatorCoordinate(0.5, 0.5, 0);
```


### Handlers
- [BoxZoomHandler](https://maplibre.org/maplibre-gl-js/docs/API/classes/maplibregl.BoxZoomHandler/)
- [DoubleClickZoomHandler](https://maplibre.org/maplibre-gl-js/docs/API/classes/maplibregl.DoubleClickZoomHandler/)
- [DragPanHandler](https://maplibre.org/maplibre-gl-js/docs/API/classes/maplibregl.DragPanHandler/)
- [DragRotateHandler](https://maplibre.org/maplibre-gl-js/docs/API/classes/maplibregl.DragRotateHandler/)
- [KeyboardHandler](https://maplibre.org/maplibre-gl-js/docs/API/classes/maplibregl.KeyboardHandler/)
- [ScrollZoomHandler](https://maplibre.org/maplibre-gl-js/docs/API/classes/maplibregl.ScrollZoomHandler/)
- [TwoFingersTouchHandler](https://maplibre.org/maplibre-gl-js/docs/API/classes/maplibregl.TwoFingersTouchHandler/)
- [TwoFingersTouchPitchHandler](https://maplibre.org/maplibre-gl-js/docs/API/classes/maplibregl.TwoFingersTouchPitchHandler/)
- [TwoFingersTouchRotateHandler](https://maplibre.org/maplibre-gl-js/docs/API/classes/maplibregl.TwoFingersTouchRotateHandler/)
- [TwoFingersTouchZoomHandler](https://maplibre.org/maplibre-gl-js/docs/API/classes/maplibregl.TwoFingersTouchZoomHandler/)
- [TwoFingersTouchZoomRotateHandler](https://maplibre.org/maplibre-gl-js/docs/API/classes/maplibregl.TwoFingersTouchZoomRotateHandler/)
```js
/** 
 * map.{Handler}.enable(options?) 
 * map.{Handler}.disable() 
 * map.{Handler}.isActive() 
 * map.{Handler}.isEnabled() 
 * map.{Handler}.{function}()
 **/


//BoxZoomHandler disable
map.boxZoom.disable();

//dragPan Enable
map.dragPan.enable({
    linearity: 0.3,
    easing: bezier(0, 0, 0.3, 1),
    maxSpeed: 1400,
    deceleration: 2500,
});

//keyboardHandler isActive
map.keyboard.isActive();

//scrollZoom setWheelZoomRate(wheelZoomRate default 1/450)
map.scrollZoom.setWheelZoomRate(1/600);


```

### Sources
- [CanvasSource](https://maplibre.org/maplibre-gl-js/docs/API/classes/maplibregl.CanvasSource/)
- [GeoJSONSource](https://maplibre.org/maplibre-gl-js/docs/API/classes/maplibregl.GeoJSONSource/)
- [ImageSource](https://maplibre.org/maplibre-gl-js/docs/API/classes/maplibregl.ImageSource/)
- [RasterDEMTileSource](https://maplibre.org/maplibre-gl-js/docs/API/classes/maplibregl.RasterDEMTileSource/)
- [RasterTileSource](https://maplibre.org/maplibre-gl-js/docs/API/classes/maplibregl.RasterTileSource/)
- [VectorTileSource](https://maplibre.org/maplibre-gl-js/docs/API/classes/maplibregl.VectorTileSource/)
- [VideoSource](https://maplibre.org/maplibre-gl-js/docs/API/classes/maplibregl.VideoSource/)
- [Source](https://maplibre.org/maplibre-gl-js/docs/API/interfaces/maplibregl.Source/)
```js
//CanvasSource
map.addSource('some id', {
   type: 'canvas',
   canvas: 'idOfMyHTMLCanvas',
   animate: true,
   coordinates: [
       [-76.54, 39.18],
       [-76.52, 39.18],
       [-76.52, 39.17],
       [-76.54, 39.17]
   ]
});

// update
let mySource = map.getSource('some id');
mySource.setCoordinates([
    [-76.54335737228394, 39.18579907229748],
    [-76.52803659439087, 39.1838364847587],
    [-76.5295386314392, 39.17683392507606],
    [-76.54520273208618, 39.17876344106642]
]);

map.removeSource('some id');  // remove

//Image
map.addSource('some id', {
   type: 'image',
   url: 'https://www.maplibre.org/images/foo.png',
   coordinates: [
       [-76.54, 39.18],
       [-76.52, 39.18],
       [-76.52, 39.17],
       [-76.54, 39.17]
   ]
});

//GeojsonSource
map.addSource('some id', {
   type: 'geojson',
   data: {
       "type": "FeatureCollection",
       "features": [{
           "type": "Feature",
           "properties": {},
           "geometry": {
               "type": "Point",
               "coordinates": [
                   -76.53063297271729,
                   39.18174077994108
               ]
           }
       }]
   }
});

//RasterTile
map.addSource('wms-test-source', {
     'type': 'raster',
// use the tiles option to specify a WMS tile source URL
     'tiles': [
         'https://img.nj.gov/imagerywms/Natural2015?bbox={bbox-epsg-3857}&format=image/png&service=WMS&version=1.1.1&request=GetMap&srs=EPSG:3857&transparent=true&width=256&height=256&layers=Natural2015'
     ],
     'tileSize': 256
});

//RasterDemTile
map.addSource('raster-dem-source', {
     type: 'raster-dem',
     url: 'https://demotiles.maplibre.org/terrain-tiles/tiles.json',
     tileSize: 256
});

//VectorTile
map.addSource('some id', {
    type: 'vector',
    tiles: ['https://d25uarhxywzl1j.cloudfront.net/v0.1/{z}/{x}/{y}.mvt'],
    minzoom: 6,
    maxzoom: 14
});

```

### Event Related
- [Evented](https://maplibre.org/maplibre-gl-js/docs/API/classes/maplibregl.Evented/)
- [MapTouchEvent](https://maplibre.org/maplibre-gl-js/docs/API/classes/maplibregl.MapTouchEvent/)
- [MapWheelEvent](https://maplibre.org/maplibre-gl-js/docs/API/classes/maplibregl.MapWheelEvent/)
- [MapContextEvent](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.MapContextEvent/)
- [MapDataEvent](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.MapDataEvent/)
- [MapEventType](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.MapEventType/)
- [MapLayerEventType](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.MapLayerEventType/)
- [MapLayerMouseEvent](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.MapLayerMouseEvent/)
- [MapLayerTouchEvent](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.MapLayerTouchEvent/)
- [MapLibreEvent](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.MapLibreEvent/)
- [MapLibreZoomEvent](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.MapLibreZoomEvent/)
- [MapSourceDataEvent](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.MapSourceDataEvent/)
- [MapStyleDataEvent](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.MapStyleDataEvent/)
- [MapStyleImageMissingEvent](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.MapStyleImageMissingEvent/)
- [MapTerrainEvent](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.MapTerrainEvent/)
```js
/**
 * map.listens('{event type}')
 * map.on('{event type}',{listener})
 * map.off('{event type}',{listener?})
 * */
//MapDataEvent
map.on('sourcedata', function(e) {
   if (e.isSourceLoaded) {
       // Do something when the source has finished loading
   }
});

//MapDataEvent
map.on('sourcedata', function(e) {
   if (e.isSourceLoaded) {
       // Do something when the source has finished loading
   }
});
/*
error: ErrorEvent;
load: MapLibreEvent;
idle: MapLibreEvent;
remove: MapLibreEvent;
render: MapLibreEvent;
resize: MapLibreEvent;
webglcontextlost: MapContextEvent;
webglcontextrestored: MapContextEvent;
dataloading: MapDataEvent;
data: MapDataEvent;
tiledataloading: MapDataEvent;
sourcedataloading: MapSourceDataEvent;
styledataloading: MapStyleDataEvent;
sourcedata: MapSourceDataEvent;
styledata: MapStyleDataEvent;
styleimagemissing: MapStyleImageMissingEvent;
dataabort: MapDataEvent;
sourcedataabort: MapSourceDataEvent;
boxzoomcancel: MapLibreZoomEvent;
boxzoomstart: MapLibreZoomEvent;
boxzoomend: MapLibreZoomEvent;
touchcancel: MapTouchEvent;
touchmove: MapTouchEvent;
touchend: MapTouchEvent;
touchstart: MapTouchEvent;
click: MapMouseEvent;
contextmenu: MapMouseEvent;
dblclick: MapMouseEvent;
mousemove: MapMouseEvent;
mouseup: MapMouseEvent;
mousedown: MapMouseEvent;
mouseout: MapMouseEvent;
mouseover: MapMouseEvent;
movestart: MapLibreEvent<MouseEvent | TouchEvent | WheelEvent | undefined>;
move: MapLibreEvent<MouseEvent | TouchEvent | WheelEvent | undefined>;
moveend: MapLibreEvent<MouseEvent | TouchEvent | WheelEvent | undefined>;
zoomstart: MapLibreEvent<MouseEvent | TouchEvent | WheelEvent | undefined>;
zoom: MapLibreEvent<MouseEvent | TouchEvent | WheelEvent | undefined>;
zoomend: MapLibreEvent<MouseEvent | TouchEvent | WheelEvent | undefined>;
rotatestart: MapLibreEvent<MouseEvent | TouchEvent | undefined>;
rotate: MapLibreEvent<MouseEvent | TouchEvent | undefined>;
rotateend: MapLibreEvent<MouseEvent | TouchEvent | undefined>;
dragstart: MapLibreEvent<MouseEvent | TouchEvent | undefined>;
drag: MapLibreEvent<MouseEvent | TouchEvent | undefined>;
dragend: MapLibreEvent<MouseEvent | TouchEvent | undefined>;
pitchstart: MapLibreEvent<MouseEvent | TouchEvent | undefined>;
pitch: MapLibreEvent<MouseEvent | TouchEvent | undefined>;
pitchend: MapLibreEvent<MouseEvent | TouchEvent | undefined>;
wheel: MapWheelEvent;
terrain: MapTerrainEvent;
 
 */
```


### Classes
- [AJAXError](https://maplibre.org/maplibre-gl-js/docs/API/classes/maplibregl.AJAXError/)
- [Actor](https://maplibre.org/maplibre-gl-js/docs/API/classes/maplibregl.Actor/)
- [CanonicalTileID](https://maplibre.org/maplibre-gl-js/docs/API/classes/maplibregl.CanonicalTileID/)
- [CircleStyleLayer](https://maplibre.org/maplibre-gl-js/docs/API/classes/maplibregl.CircleStyleLayer/)
- [ClickZoomHandler](https://maplibre.org/maplibre-gl-js/docs/API/classes/maplibregl.ClickZoomHandler/)
- [Dispatcher](https://maplibre.org/maplibre-gl-js/docs/API/classes/maplibregl.Dispatcher/)
- [Event](https://maplibre.org/maplibre-gl-js/docs/API/classes/maplibregl.Event/)
- [GeoJSONFeature](https://maplibre.org/maplibre-gl-js/docs/API/classes/maplibregl.GeoJSONFeature/)
- [HeatmapStyleLayer](https://maplibre.org/maplibre-gl-js/docs/API/classes/maplibregl.HeatmapStyleLayer/)
- [Layout](https://maplibre.org/maplibre-gl-js/docs/API/classes/maplibregl.Layout/)
- [MapMouseEvent](https://maplibre.org/maplibre-gl-js/docs/API/classes/maplibregl.MapMouseEvent/)
- [OverscaledTileID](https://maplibre.org/maplibre-gl-js/docs/API/classes/maplibregl.OverscaledTileID/)
- [RGBAImage](https://maplibre.org/maplibre-gl-js/docs/API/classes/maplibregl.RGBAImage/)
- [Style](https://maplibre.org/maplibre-gl-js/docs/API/classes/maplibregl.Style/)
- [StyleLayer](https://maplibre.org/maplibre-gl-js/docs/API/classes/maplibregl.StyleLayer/)
- [ThrottledInvoker](https://maplibre.org/maplibre-gl-js/docs/API/classes/maplibregl.ThrottledInvoker/)
- [WorkerPool](https://maplibre.org/maplibre-gl-js/docs/API/classes/maplibregl.WorkerPool/)

### Enumerations
- [ResourceType](https://maplibre.org/maplibre-gl-js/docs/API/enums/maplibregl.ResourceType/)

### Events
- [FullscreenControl](https://maplibre.org/maplibre-gl-js/docs/API/classes/maplibregl.FullscreenControl/)
- [GeolocateControl](https://maplibre.org/maplibre-gl-js/docs/API/classes/maplibregl.GeolocateControl/)
- [Marker](https://maplibre.org/maplibre-gl-js/docs/API/classes/maplibregl.Marker/)
- [Popup](https://maplibre.org/maplibre-gl-js/docs/API/classes/maplibregl.Popup/)
- [Source](https://maplibre.org/maplibre-gl-js/docs/API/interfaces/maplibregl.Source/)

### Interfaces
- [AttributeBinder](https://maplibre.org/maplibre-gl-js/docs/API/interfaces/maplibregl.AttributeBinder/)
- [Bucket](https://maplibre.org/maplibre-gl-js/docs/API/interfaces/maplibregl.Bucket/)
- [CustomLayerInterface](https://maplibre.org/maplibre-gl-js/docs/API/interfaces/maplibregl.CustomLayerInterface/)
- [Handler](https://maplibre.org/maplibre-gl-js/docs/API/interfaces/maplibregl.Handler/)
- [IControl](https://maplibre.org/maplibre-gl-js/docs/API/interfaces/maplibregl.IControl/)
- [StyleImageInterface](https://maplibre.org/maplibre-gl-js/docs/API/interfaces/maplibregl.StyleImageInterface/)

### Type Aliases
- [AddLayerObject](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.AddLayerObject/)
- [Alignment](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.Alignment/)
- [AnimationOptions](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.AnimationOptions/)
- [AroundCenterOptions](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.AroundCenterOptions/)
- [AttributionOptions](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.AttributionOptions/)
- [Callback](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.Callback/)
- [CameraForBoundsOptions](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.CameraForBoundsOptions/)
- [CameraOptions](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.CameraOptions/)
- [CameraUpdateTransformFunction](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.CameraUpdateTransformFunction/)
- [Cancelable](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.Cancelable/)
- [CanvasSourceSpecification](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.CanvasSourceSpecification/)
- [CenterZoomBearing](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.CenterZoomBearing/)
- [Config](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.Config/)
- [ControlPosition](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.ControlPosition/)
- [Coordinates](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.Coordinates/)
- [CrossFaded](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.CrossFaded/)
- [CustomRenderMethod](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.CustomRenderMethod/)
- [DashEntry](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.DashEntry/)
- [DistributiveKeys](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.DistributiveKeys/)
- [DistributiveOmit](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.DistributiveOmit/)
- [DragPanOptions](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.DragPanOptions/)
- [ErrorCallback](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.ErrorCallback/)
- [ExpiryData](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.ExpiryData/)
- [FeatureIdentifier](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.FeatureIdentifier/)
- [FitBoundsOptions](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.FitBoundsOptions/)
- [FlyToOptions](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.FlyToOptions/)
- [FullscreenOptions](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.FullscreenOptions/)
- [GeoJSONFeatureDiff](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.GeoJSONFeatureDiff/)
- [GeoJSONFeatureId](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.GeoJSONFeatureId/)
- [GeoJSONSourceDiff](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.GeoJSONSourceDiff/)
- [GeolocateOptions](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.GeolocateOptions/)
- [GestureOptions](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.GestureOptions/)
- [GetImageCallback](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.GetImageCallback/)
- [GlyphMetrics](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.GlyphMetrics/)
- [GlyphPosition](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.GlyphPosition/)
- [GlyphPositions](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.GlyphPositions/)
- [GridKey](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.GridKey/)
- [HandlerResult](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.HandlerResult/)
- [JumpToOptions](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.JumpToOptions/)
- [Listener](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.Listener/)
- [LogoOptions](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.LogoOptions/)
- [MapGeoJSONFeature](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.MapGeoJSONFeature/)
- [MapOptions](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.MapOptions/)
- [MapSourceDataType](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.MapSourceDataType/)
- [MarkerOptions](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.MarkerOptions/)
- [NavigationOptions](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.NavigationOptions/)
- [Offset](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.Offset/)
- [OverlapMode](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.OverlapMode/)
- [PositionAnchor](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.PositionAnchor/)
- [PossiblyEvaluatedValue](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.PossiblyEvaluatedValue/)
- [QueryRenderedFeaturesOptions](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.QueryRenderedFeaturesOptions/)
- [QuerySourceFeatureOptions](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.QuerySourceFeatureOptions/)
- [Rect](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.Rect/)
- [RequestParameters](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.RequestParameters/)
- [RequestTransformFunction](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.RequestTransformFunction/)
- [RequireAtLeastOne](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.RequireAtLeastOne/)
- [ResponseCallback](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.ResponseCallback/)
- [ScaleOptions](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.ScaleOptions/)
- [SerializedStructArray](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.SerializedStructArray/)
- [SetClusterOptions](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.SetClusterOptions/)
- [SourceClass](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.SourceClass/)
- [SourceStatics](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.SourceStatics/)
- [SpriteOnDemandStyleImage](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.SpriteOnDemandStyleImage/)
- [StyleImage](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.StyleImage/)
- [StyleImageData](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.StyleImageData/)
- [StyleImageMetadata](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.StyleImageMetadata/)
- [StyleOptions](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.StyleOptions/)
- [StyleSetterOptions](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.StyleSetterOptions/)
- [StyleSwapOptions](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.StyleSwapOptions/)
- [SymbolQuad](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.SymbolQuad/)
- [TileState](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.TileState/)
- [Transferable](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.Transferable/)
- [TransformStyleFunction](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.TransformStyleFunction/)
- [Unit](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.Unit/)
- [UpdateImageOptions](https://maplibre.org/maplibre-gl-js/docs/API/types/maplibregl.UpdateImageOptions/)
