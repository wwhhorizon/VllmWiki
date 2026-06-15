# vllm-project/vllm#1694: using vllm to answer in Qwen-7B-Chat, there is a recurring issue of answers being repeated multiple times,

| 字段 | 值 |
| --- | --- |
| Issue | [#1694](https://github.com/vllm-project/vllm/issues/1694) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> using vllm to answer in Qwen-7B-Chat, there is a recurring issue of answers being repeated multiple times,

### Issue 正文摘录

When using vllm to answer in Qwen-7B-Chat, there is a recurring issue of answers being repeated multiple times, which is not present when not using vllm. GPU: 2 T4 MODEL: Qwen-7B-Chat PROMPT: 根据已知信息，简洁和专业的来回答问题。如果无法从中得到答案，请说 \n\"根据已知信息无法回答该问题，请使用随手拍进行提问，随手拍使用路径：手机移动办公-工作台-数字直通车\"。不允许在答案中添加编造成分，答案请使用中文，结果以markdown的形式输出。 \n\n 问题：是否可以先开户、后面再补上门核实和法人开户意愿核实工作？ 答案：上门核实可以后补，法人开户意愿核实需要提前或同步完成。\n问题：客户签约财资需要哪几个步骤（大步骤，具体的步骤可以参考操作文档） 答案：1、客户确认签约财资的方案；\n2、上级单位与下级单位完成账户使用授权（如无下级单位或关联单位，则跳过这一步）；\n3、在前台签署相关协议，录入系统；\n4、经办行引导客户登录财资，并协助客户配置相关设置及参数；\n问题：营业执照刚刚注册好，工商系统还查不到，能开户吗？ 答案：在风险可控的情况下，确定客户开户信息真实，可以开户。 \n\n 企业开户流程

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: using vllm to answer in Qwen-7B-Chat, there is a recurring issue of answers being repeated multiple times, When using vllm to answer in Qwen-7B-Chat, there is a recurring issue of answers being repeated multiple times,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
