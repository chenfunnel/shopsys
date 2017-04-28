// JavaScript Document
    //创建和初始化地图函数：
 var map = new BMap.Map("container");
    map.centerAndZoom("西安", 12);
    map.enableScrollWheelZoom();    //启用滚轮放大缩小，默认禁用
    map.enableContinuousZoom();    //启用地图惯性拖拽，默认禁用

    map.addControl(new BMap.NavigationControl());  //添加默认缩放平移控件
    map.addControl(new BMap.OverviewMapControl()); //添加默认缩略地图控件
    map.addControl(new BMap.OverviewMapControl({ isOpen: true, anchor: BMAP_ANCHOR_BOTTOM_RIGHT }));   //右下角，打开

    //var localSearch = new BMap.LocalSearch(map);
    //localSearch.enableAutoViewport(); //允许自动调节窗体大小

function searchByStationName() {
	var map = new BMap.Map("container");	
	//map.clearOverlays();//清空原来的标注	
 	var city = document.getElementById("city_").value
	map.centerAndZoom(city, 12);
	map.enableScrollWheelZoom();    //启用滚轮放大缩小，默认禁用
    map.enableContinuousZoom();    //启用地图惯性拖拽，默认禁用

    map.addControl(new BMap.NavigationControl());  //添加默认缩放平移控件
    map.addControl(new BMap.OverviewMapControl()); //添加默认缩略地图控件
    map.addControl(new BMap.OverviewMapControl({ isOpen: true, anchor: BMAP_ANCHOR_BOTTOM_RIGHT }));   //右下角，打开
	//查询
	var localSearch = new BMap.LocalSearch(map, {renderOptions: {map: map, panel: "results_info"}});
    localSearch.enableAutoViewport(); //允许自动调节窗体大小	
	
	var keyword = document.getElementById("text_").value;
		localSearch.setSearchCompleteCallback(function (searchResult) {
        var poi = searchResult.getPoi(0);
		//alert (poi.point.lng + "," + poi.point.lat);
        document.getElementById("result_").value = poi.point.lng + "," + poi.point.lat;
        map.centerAndZoom(poi.point, 15);
        var marker = new BMap.Marker(new BMap.Point(poi.point.lng, poi.point.lat));  // 创建标注，为要查询的地方对应的经纬度
        map.addOverlay(marker);
        var content = document.getElementById("text_").value + "<br/><br/>经度：" + poi.point.lng + "<br/>纬度：" + poi.point.lat;
        var infoWindow = new BMap.InfoWindow("<p style='font-size:14px;'>" + content + "</p>");
        marker.addEventListener("click", function () { this.openInfoWindow(infoWindow); });
        // marker.setAnimation(BMAP_ANIMATION_BOUNCE); //跳动的动画
    });
    localSearch.search(keyword);
} 
//弹出隐藏层  
  	
function openLogin(){
   document.getElementById("win").style.display="";
}
function closeLogin(){
   document.getElementById("win").style.display="none";
}

function MblogDotccMap(){  
    var map = new BMap.Map("container");          // 创建地图实例    
    var point = new BMap.Point(119.607568,39.940628);  // 创建点坐标    
    var keyword = document.getElementById("text_").value;  
    map.centerAndZoom(point, 17);                 // 初始化地图，设置中心点坐标和地图级别    
      
    //添加缩放控件  
    map.addControl(new BMap.NavigationControl());    
    map.addControl(new BMap.ScaleControl());    
    map.addControl(new BMap.OverviewMapControl());   
      
    /*显示地图中心地点的坐标 
    map.addEventListener("dragend", function(){ 
      //map.panTo(point); 
      var center = map.getCenter(); 
      document.getElementById("info").innerHTML = "当前地图中心坐标：" + center.lng + ", " + center.lat; 
    });*/  
      
    //搜索  
    var local = new BMap.LocalSearch(map, {renderOptions: {map: map, panel: "results_info"}});  
    map.panBy(point);  
    local.search(keyword);   
    local.getResults();  
    local.setSearchCompleteCallback(function(searchResult){  
            var poi = searchResult.getPoi(0);  
            alert(poi.point.lng+"   "+poi.point.lat);  
            document.getElementById("result_").value = poi.point.lng + "," + poi.point.lat;  
    });  
  
  
    map.addEventListener("click", function (e) {  
            var _point = e.point;  
            document.getElementById("result_").value = _point.lng + "," + _point.lat;  
          
    });  
  
} 