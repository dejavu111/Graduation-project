package com.qust.employment.po;

/**
 * @author ：dejavu111
 * @date ：Created in 2019/4/1 15:31
 * @description：
 * @modified By：
 * @version: $
 */
public class DetailInfo {
    private Integer id;

    private String uuid;

    private String detailUrl;

    private String title;

    private String location;

    private String holdTime;

    private String siteName;

    private String content;

    private String companyInfo;

    private Integer isparsed;

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getUuid() {
        return uuid;
    }

    public void setUuid(String uuid) {
        this.uuid = uuid;
    }

    public String getDetailUrl() {
        return detailUrl;
    }

    public void setDetailUrl(String detailUrl) {
        this.detailUrl = detailUrl;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }

    public String getHoldTime() {
        return holdTime;
    }

    public void setHoldTime(String holdTime) {
        this.holdTime = holdTime;
    }

    public String getSiteName() {
        return siteName;
    }

    public void setSiteName(String siteName) {
        this.siteName = siteName;
    }

    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }

    public String getCompanyInfo() {
        return companyInfo;
    }

    public void setCompanyInfo(String companyInfo) {
        this.companyInfo = companyInfo;
    }

    public Integer getIsparsed() {
        return isparsed;
    }

    public void setIsparsed(Integer isparsed) {
        this.isparsed = isparsed;
    }

    @Override
    public String toString() {
        return "DetailInfo{" +
                "id=" + id +
                ", uuid='" + uuid + '\'' +
                ", detailUrl='" + detailUrl + '\'' +
                ", title='" + title + '\'' +
                ", location='" + location + '\'' +
                ", holdTime='" + holdTime + '\'' +
                ", siteName='" + siteName + '\'' +
                ", content='" + content + '\'' +
                ", companyInfo='" + companyInfo + '\'' +
                ", isparsed=" + isparsed +
                '}';
    }
}
