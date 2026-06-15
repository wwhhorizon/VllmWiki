# vllm-project/vllm#32338: [Feature]: support for LlavaQwenForCausalLM

| 字段 | 值 |
| --- | --- |
| Issue | [#32338](https://github.com/vllm-project/vllm/issues/32338) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: support for LlavaQwenForCausalLM

### Issue 正文摘录

### 🚀 The feature, motivation and pitch vllm is a great work!! but there are some models have not been supported yet. "Value error, Model architectures ['LlavaQwenForCausalLM'] are not supported for now."vllm version is 0.13.0 Now many llava-series models have LlavaQwenForCausalLM model architectures,such as [llava-video-7b-qwen2](https://huggingface.co/collections/lmms-lab/llava-video)，[llava-onevision](https://huggingface.co/collections/lmms-lab/llava-onevision). Could these models be supported? The whole error are as following: ``` INFO 01-14 23:42:54 [utils.py:253] non-default args: {'trust_remote_code': True, 'max_model_len': 8192, 'gpu_memory_utilization': 0.6, 'disable_log_stats': True, 'model': '/lpai/volumes/base-3da-ali-sh-mix/zzz_sh/repos/3d4mllm/LLaVA-NeXT-origin/LLaVA-Video-7B-Qwen2'} The argument `trust_remote_code` is to be used with Auto classes. It has no effect here and is ignored. Traceback (most recent call last): File " ", line 2, in File "/lpai/volumes/base-3da-ali-sh-mix/zzz_sh/envs/easyr1-tor280-vllm0130-cu129-py311/lib/python3.11/site-packages/vllm/entrypoints/llm.py", line 351, in __init__ self.llm_engine = LLMEngine.from_engine_args( ^^^^^^^^^^^^^^^^^^^^...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 11: [Feature]: support for LlavaQwenForCausalLM feature request;stale ### 🚀 The feature, motivation and pitch vllm is a great work!! but there are some models have not been supported yet. "Value error, Model architectures [...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: l architectures ['LlavaQwenForCausalLM'] are not supported for now."vllm version is 0.13.0 Now many llava-series models have LlavaQwenForCausalLM model architectures,such as [llava-video-7b-qwen2](https://huggingface.co...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: there are some models have not been supported yet. "Value error, Model architectures ['LlavaQwenForCausalLM'] are not supported for now."vllm version is 0.13.0 Now many llava-series models have LlavaQwenForCausalLM mode...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: alLM'] are not supported for now. Supported architectures: dict_keys(['AfmoeForCausalLM', 'ApertusForCausalLM', 'AquilaModel', 'AquilaForCausalLM', 'ArceeForCausalLM', 'ArcticForCausalLM', 'BaiChuanForCausalLM', 'Baichu...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: support for LlavaQwenForCausalLM feature request;stale ### 🚀 The feature, motivation and pitch vllm is a great work!! but there are some models have not been supported yet. "Value error, Model architectures [...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
