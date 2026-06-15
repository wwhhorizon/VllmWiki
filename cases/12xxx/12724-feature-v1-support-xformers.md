# vllm-project/vllm#12724: [Feature]: V1 support Xformers

| 字段 | 值 |
| --- | --- |
| Issue | [#12724](https://github.com/vllm-project/vllm/issues/12724) |
| 状态 | closed |
| 标签 | feature request;stale;v1 |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: V1 support Xformers

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I tried to use V1 engine to load Qwen2.5-72B-Instruct-GPTQ-int4 on 4*2080ti 22g, and it raised an AssertionError. The error message shows assert is_fa_version_supported(self.fa_version) caused this AssertionError. It seems like the 2080ti does not support any version of FA. In the V0 engine, it uses the Xformers backend and works fine. However, in V1, it raises an error and stops working. So, I would like to request Xformers support for the V1 engine. I know the 2080ti is a bit outdated, but it is the only choice for getting a large GPU memory at an acceptable price. I really appreciate your help with this. It would mean a lot. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: g, and it raised an AssertionError. The error message shows assert is_fa_version_supported(self.fa_version) caused this AssertionError. It seems like the 2080ti does not support any version of FA. In the V0 engine, it u...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: V1 support Xformers feature request;stale;v1 ### 🚀 The feature, motivation and pitch I tried to use V1 engine to load Qwen2.5-72B-Instruct-GPTQ-int4 on 4*2080ti 22g, and it raised an AssertionError. The error...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: es not support any version of FA. In the V0 engine, it uses the Xformers backend and works fine. However, in V1, it raises an error and stops working. So, I would like to request Xformers support for the V1 engine. I kn...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: on and pitch I tried to use V1 engine to load Qwen2.5-72B-Instruct-GPTQ-int4 on 4*2080ti 22g, and it raised an AssertionError. The error message shows assert is_fa_version_supported(self.fa_version) caused this Assertio...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
