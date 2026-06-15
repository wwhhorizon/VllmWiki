# vllm-project/vllm#8805: [Bug]: vllm api server return escaped unicode string in guided backend 'outlines' 

| 字段 | 值 |
| --- | --- |
| Issue | [#8805](https://github.com/vllm-project/vllm/issues/8805) |
| 状态 | closed |
| 标签 | bug;structured-output;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vllm api server return escaped unicode string in guided backend 'outlines' 

### Issue 正文摘录

### Environment vllm/vllm-openai:v0.6.1.post2 vllm/vllm-openai:v0.6.0 vllm/vllm-openai:v0.5.5 vllm/vllm-openai:v0.5.0.post1 ### Problems Run the following code on different version of vllm,the result differs. - As for version 0.5.5 and 0.6.x(0.6.0 ,0.6.1post2),i got the strange result which contains serveral unicode string values as following (outlines==0.0.46): ```Json [{"trigger": "IPO", "event_type": "\u516c\u53f8\u4e0a\u5e02", "arguments": [{"role": "\u4e0a\u5e02\u516c\u53f8", "argument": "\\\\u7406\\\\u601f\\\\u6c7d\\\\u8f66"}, {"role": "\u73af\u8282", "argument": "\\\\u7b80\\\\u5185\\\\u62db\\\\u8282"}, {"role": "\u62ab\u9732\u65f6\u95f4", "argument": "\\\\u7f8e\\\\u56fd\\\\u9996\\\\u6b21\\\\u516c\\\\u5f00\\\\u52d8\\\\u8001"}, {"role": "\u62ab\u9732\u65f6\u95f4", "argument": "\\\\u81ea\\\\u7136\\\\u5e74"}, {"role": "\u53d1\u884c\u4ef7\u683c", "argument": "\\\\u6bcf\\\\u80a18-10\\\\u7f8e\\\\u5143"}, {"role": "\u5e02\u503c", "argument": "\\\\u975e\\\\u5e38\\\\u672a\\\\u63d2\\\\u4f9b"}, {"role": "\u5e02\u503c", "argument": "\\\\u975e\\\\u5e38\\\\u672a\\\\u63d2\\\\u4f9b"}]}] ``` - As for version 0.5.0.post1 (outlines==0.0.43) ,i got the expected result : ```Json [{"trigger": "IP...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: : "事件时间", "argument": "未提及具体日期"}]}] ``` Here is the test code ```Python MODEL_NAME = '...' client = OpenAI(api_key='api_key', base_url='') client.base_url = 'http://$local_vllm_server_address/v1/' prompt = """ # 角色 你是一个...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: caped unicode string in guided backend 'outlines' bug;structured-output;stale ### Environment vllm/vllm-openai:v0.6.1.post2 vllm/vllm-openai:v0.6.0 vllm/vllm-openai:v0.5.5 vllm/vllm-openai:v0.5.0.post1 ### Problems Run...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Bug]: vllm api server return escaped unicode string in guided backend 'outlines' bug;structured-output;stale ### Environment vllm/vllm-openai:v0.6.1.post2 vllm/vllm-openai:v0.6.0 vllm/vllm-openai:v0.5.5 vllm/vllm-opena...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: lm-openai:v0.5.0.post1 ### Problems Run the following code on different version of vllm,the result differs. - As for version 0.5.5 and 0.6.x(0.6.0 ,0.6.1post2),i got the strange result which contains serveral unicode st...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: e texts (sth like duplicates string segments,looks like a early greedy search 'pitfall'?). Everytime a restart will bring it back to normal . Is this a bug? Fixed in the latest release? Here is my vllm start commands: `...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
