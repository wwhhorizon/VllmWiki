# vllm-project/vllm#15919: [Bug]: Replies suddenly stop,  Qwen2.5-VL-72B Poor response quality

| 字段 | 值 |
| --- | --- |
| Issue | [#15919](https://github.com/vllm-project/vllm/issues/15919) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Replies suddenly stop,  Qwen2.5-VL-72B Poor response quality

### Issue 正文摘录

### Your current environment 我使用vllm 0.7.4和0.8.2来部署qwen2.5-VL-72B都会出现问题，在一些case上无法正常输出，最后回退到了一个0.7.2dev版本，这里有一个示例，只有在0.7.2dev上可以正常回答。镜像是从https://github.com/hiyouga/EasyR1/tree/main获取的 - docker pull hiyouga/verl:ngc-th2.5.1-cu120-vllm0.7.4-hotfix - docker pull hiyouga/verl:ngc-th2.6.0-cu120-vllm0.8.2 请求示例：[exapmle.txt](https://github.com/user-attachments/files/19560634/exapmle.txt)

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: 只有在0.7.2dev上可以正常回答。镜像是从https://github.com/hiyouga/EasyR1/tree/main获取的 - docker pull hiyouga/verl:ngc-th2.5.1-cu120-vllm0.7.4-hotfix - docker pull hiyouga/verl:ngc-th2.6.0-cu120-vllm0.8.2 请求示例：[exapmle.txt](https://githu...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Replies suddenly stop, Qwen2.5-VL-72B Poor response quality bug ### Your current environment 我使用vllm 0.7.4和0.8.2来部署qwen2.5-VL-72B都会出现问题，在一些case上无法正常输出，最后回退到了一个0.7.2dev版本，这里有一个示例，只有在0.7.2dev上可以正常回答。镜像是从https://git...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: nd_api;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error env_dependency Your current environment
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: arallel;frontend_api;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error env_dependency Your current environment
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: i_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
