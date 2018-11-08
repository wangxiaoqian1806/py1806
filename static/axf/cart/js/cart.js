$(function () {

    $(".confirm").click(function () {
        $current_btn = $(this);
        // 知道点的是谁
        var c_id = $(this).parents("li").attr("c_id");
        //
        $.ajax({
            url: "/axf/cart_status",
            data: {
                c_id: c_id
            },
            method: "patch",
            success: function (res) {
                console.log(res);
                if (res.code == 1) {
                    //
                    if (res.data.status) {
                        $current_btn.find("span").find("span").html("√");

                    } else {
                        $current_btn.find("span").find("span").html("");

                    }
                    //
                    $("#money_id").html(res.data.sum_money);

                    //
                    if (res.data.is_select_all) {
                        $(".all_select > span > span").html("√");
                    }else{
                        $(".all_select > span > span").html("");
                    }
                }

            }
        })

    });

    $(".all_select").click(function () {
        $.ajax({
            url:"/axf/cart_all_status",
            data:{

            },
            method:"put",
            success:function (res) {
                console.log(res);
                if (res.code == 1){
                //
                    $("#money_id").html(res.data.sum_money);
                    if (res.data.all_select){
                        $(".all_select > span > span").html("√")
                        $(".confirm").each(function () {
                            $(this).find("span").find("span").html("√");


                        })
                    } else{
                        $(".all_select > span > span").html("");
                        $(".confirm").each(function () {
                            $(this).find("span").find("span").html("");


                        })

                    }
                }

            }

        })


    });

    $(".addBtn").click(function () {
        $current_btn = $(this);
        // 知道点的是谁
        var c_id = $(this).parents("li").attr("c_id");
        //
        $.ajax({
            url: "/axf/cart_item",
            data: {
                c_id: c_id
            },
            method: "post",
            success: function (res) {

                if (res.code == 1){

                    $("#money_id").html(res.data.sum_money);

                    $current_btn.prev().html(res.data.num);

                }else{
                    alert(res.msg);
                }

            }
        })
    });

    $(".subBtn").click(function () {

        var $current_btn = $(this);
    //
        var c_id = $(this).parents("li").attr("c_id");


        $.ajax({
            url:"/axf/cart_item",
            data:{
                c_id:c_id
            },
            method:"delete",
            success:function (res) {
                if (res.code == 1){
                    if (res.data.num == 0){
                        //
                        $current_btn.parents("li").remove();
                    }else{
                        $current_btn.next().html(res.data.num);
                    }
                    //
                    $("#money_id").html(res.data.sum_money);

                }else{
                    alert(res.msg);
                }

            }
        })

    });

    $("#order").click(function () {
        var money = $("#money_id").html();
        if (money == "0"){
            alert("暂无商品可以下单");

        }else{
            window.open("/axf/order",target="_self");
        }

    })


})



















