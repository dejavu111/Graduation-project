package com.qust.employment.utils;

import com.alibaba.fastjson.JSONObject;
import com.google.common.base.Strings;
import com.google.gson.Gson;
import com.qust.employment.Constant.Constants;


import java.math.BigDecimal;
import java.time.*;

public class Utils {
    private Utils(){}

    public static boolean isToday(String date){
        if (Strings.isNullOrEmpty(date)){
            return false;
        }

        LocalDate localDate =  LocalDate.parse(date);
        LocalDate todayDate = LocalDate.now();

        return localDate.isEqual(todayDate);
    }

    public static boolean isThisYear(String date){
        if (Strings.isNullOrEmpty(date)){
            return false;
        }

        LocalDate localDate =  LocalDate.parse(date);
        LocalDate todayDate = LocalDate.now();

        return localDate.getYear() == todayDate.getYear();
    }


    /**
     * 处理小数
     * @param digits 要保留小数位数
     * @return
     */
    public static String processDecimal(String number, int digits){
        if(number.contains(".")){
            BigDecimal bigDecimal = new BigDecimal(number);
            bigDecimal = bigDecimal.setScale(digits, BigDecimal.ROUND_HALF_UP);

            return bigDecimal.toString();
        }

        return number;
    }


    public static String toResultJson(int code, String msg){
        JSONObject resultJson = new JSONObject();

        resultJson.put("code", code);

        if (Constants.FAIL_CODE == code) {
            resultJson.put("msg", msg);
        }

        return resultJson.toString();

    }

    public static String toResultJson(int code, String msg, Object obj){
        JSONObject resultJson = new JSONObject();
        Gson resultGson = new Gson();

        resultJson.put("code", code);

        if (Constants.SUCCESS_CODE == code) {
            if(obj != null){
                resultJson.put("data", resultGson.toJson(obj));
            }else{
                resultJson.put("data", "");
            }

        } else {
            resultJson.put("msg", msg);
        }

        return resultJson.toString();

    }

    public static String toResultJson(int code, String msg, Object obj, int pages){
        JSONObject resultJson = new JSONObject();
        Gson resultGson = new Gson();

        resultJson.put("code", code);

        if (Constants.SUCCESS_CODE == code) {
            if(obj != null){
                resultJson.put("data", resultGson.toJson(obj));
            }else{
                resultJson.put("data", "");
            }
            resultJson.put("data", resultGson.toJson(obj));
            resultJson.put("pages", pages);
        } else {
            resultJson.put("msg", msg);
        }

        return resultJson.toString();
    }


}
