package com.qust.employment.service.Impl;

import com.qust.employment.Constant.Constants;
import com.qust.employment.mapper.DetailInfoMapper;
import com.qust.employment.po.DetailInfo;
import com.qust.employment.service.IDetailInfoService;
import com.qust.employment.utils.Utils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

/**
 * @author ：dejavu111
 * @date ：Created in 2019/4/1 16:16
 * @description：
 * @modified By：
 * @version: $
 */
@Service
public class DetailInfoService implements IDetailInfoService {
    @Autowired
    private DetailInfoMapper detailInfoMapper;
    @Override
    public String getDetailInfo(String uuid) {

        DetailInfo detailInfo = detailInfoMapper.selectByUUID(uuid);
        return Utils.toResultJson(Constants.SUCCESS_CODE,"",detailInfo);

    }
}
