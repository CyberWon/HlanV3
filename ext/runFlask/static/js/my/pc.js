function getIPGroup(){
	var url="/ga/DownloadCheck/api";
	var e= [{
	    text: "全国",
	    href: "#P0",
	    nodes: [{
            text: "北京",
            href: "#P1",
        		},{
	                text: "天津",
	                href: "#P2",
	            },{
	                text: "河北",
	                href: "#P3",
	            },{
	                text: "山西",
	                href: "#P4",
	            },{
	                text: "内蒙古",
	                href: "#P5",
	            },{
	                text: "辽宁",
	                href: "#P6",
	            },{
	                text: "吉林",
	                href: "#P7",
	            },{
	                text: "黑龙江",
	                href: "#P8",
	            },{
	                text: "上海",
	                href: "#P9",
	            },{
	                text: "江苏",
	                href: "#P10",
	            },{
	                text: "浙江",
	                href: "#P11",
	            },{
	                text: "安徽",
	                href: "#P12",
	            },{
	                text: "福建",
	                href: "#P13",
	            },{
	                text: "江西",
	                href: "#P14",
	            },{
	                text: "山东",
	                href: "#P15",
	            },{
	                text: "河南",
	                href: "#P16",
	            },{
	                text: "湖北",
	                href: "#P17",
	            },{
	                text: "湖南",
	                href: "#P18",
	            },{
	                text: "广东",
	                href: "#P19",
	            },{
	                text: "广西",
	                href: "#P20",
	            },{
	                text: "海南",
	                href: "#P21",
	            },
	            {
	                text: "重庆",
	                href: "#P22",
	            },
	            {
	                text: "四川",
	                href: "#P23",
	            },
	            {
	                text: "贵州",
	                href: "#P24",
	            },
	            {
	                text: "云南",
	                href: "#P25",
	            },{
	                text: "西藏",
	                href: "#P26",
	            },{
	                text: "陕西",
	                href: "#P27",
	            },{
	                text: "甘肃",
	                href: "#P28",
	            },{
	                text: "青海",
	                href: "#P29",
	            },{
	                text: "宁夏",
	                href: "#P30",
	            },{
	                text: "新疆",
	                href: "#P31",
	            }]
	}];
	$("#ipgroup").treeview({
        levels: 1,
        data: e,
        onNodeSelected: function(e, o) {
            var url="/ga/DownloadCheck/api";
        	$.get(url,{m:"ipgroup",c:o.href},
        	        function(data,status){
        					$("#txtip").val(data)
        	            }   
        	        );
        }
    })
}