# vllm-project/vllm#14696: [Feature]: Support gemma3 architecture

| 字段 | 值 |
| --- | --- |
| Issue | [#14696](https://github.com/vllm-project/vllm/issues/14696) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 56; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support gemma3 architecture

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I am using vLLM for hosting of LLMs/SLMs and with the recent release of Gemma 3, I would love to have it supported in vLLM. Google has stated Gemma 3 has day 1 support from HF Transformers, so it should (hopefully) be relatively simple to integrate into vLLM. Currently, when attempting to load google/gemma-3-12b-it, the following error is given: ``` ERROR 03-12 18:19:00 engine.py:400] ValueError: The checkpoint you are trying to load has model type `gemma3` but Transformers does not recognize this architecture. This could be because of an issue with the checkpoint, or because your version of Transformers is out of date. ERROR 03-12 18:19:00 engine.py:400] ERROR 03-12 18:19:00 engine.py:400] You can update Transformers with the command `pip install --upgrade transformers`. If this does not work, and the checkpoint is very new, then there may not be a release version that supports this model yet. In this case, you can get the most up-to-date code by installing Transformers from source with the command `pip install git+https://github.com/huggingface/transformers.git` ``` ### Alternatives _No response_ ### Additional context https://blog.google/...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Feature]: Support gemma3 architecture feature request ### 🚀 The feature, motivation and pitch I am using vLLM for hosting of LLMs/SLMs and with the recent release of Gemma 3, I would love to have it supported in vLLM....
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: . This could be because of an issue with the checkpoint, or because your version of Transformers is out of date. ERROR 03-12 18:19:00 engine.py:400] ERROR 03-12 18:19:00 engine.py:400] You can update Transformers with t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Feature]: Support gemma3 architecture feature request ### 🚀 The feature, motivation and pitch I am using vLLM for hosting of LLMs/SLMs and with the recent release of Gemma 3, I would love to have it supported in vLLM....
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Feature]: Support gemma3 architecture feature request ### 🚀 The feature, motivation and pitch I am using vLLM for hosting of LLMs/SLMs and with the recent release of Gemma 3, I would love to have it supported in vLLM....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Support gemma3 architecture feature request ### 🚀 The feature, motivation and pitch I am using vLLM for hosting of LLMs/SLMs and with the recent release of Gemma 3, I would love to have it supported in vLLM....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
