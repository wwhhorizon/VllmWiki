# vllm-project/vllm#9283: [Bug]: Simultaneous mm calls lead to permanently degraded performance.

| 字段 | 值 |
| --- | --- |
| Issue | [#9283](https://github.com/vllm-project/vllm/issues/9283) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 21; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;gemm;moe;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Simultaneous mm calls lead to permanently degraded performance.

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I don't know whether this is user error, or a bug. But I'm doing multimodal inference and I noticed I could have multiple instances of my script making calls to the model and each would get the same throughput, leading to a higher avg generation throughput. Having noticed this I modified my script to make it asynchronous. But when I run it the avg generation throughput is now worse than if I was just running one instance. And when I go back to running just a single synchronous instance I'm now getting even worse throughput. The only way to get it to return to it's original performance is to restart the model. I have however noticed that if the calls are still asynchronous, but have a staggered delay to them I have no problems. To clarify with some rough numbers, the below are the results of running the different scripts against a single vllm server. | script setup | avg gen throughput (tokens/s) | |-------|--------| | A single synchronous instance | ~50 | | 3 manually started synchronous instances *(running at the same time in different terminals)* | ~150 | | 1 asynchronous instance making 3 ca...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ese it appears that something about the way I'm running the asynchronous version hits some sort of "resource limit" and so the amount of resources each call is assigned are limited *(15 \* 3 = 45)*. But when running aga...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: tly degraded performance. bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I don't know whether this is user error, or a bug. But I'm doing multimodal inference and I not...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: emote-code --limit-mm-per-prompt image=2 --gpu-memory-utilization 0.95 --quantization fp8 ``` Code: ```python import asyncio from langchain_core.prompts import ChatPromptTemplate from langchain_core.messages import Syst...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: is assigned are limited *(15 \* 3 = 45)*. But when running again with a smaller load this "call limit" is still in place. Maybe? Possibly supporting this theory is the fact that when I run the staggered version the vram...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: PromptTemplate.from_messages([ SystemMessage(content="You are an expert long format writer."), ( "user", [ { "type": "image_url", "image_url": { "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisc...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
