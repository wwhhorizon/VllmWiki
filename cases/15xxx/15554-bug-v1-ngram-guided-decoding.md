# vllm-project/vllm#15554: [Bug][V1]: ngram + guided decoding

| 字段 | 值 |
| --- | --- |
| Issue | [#15554](https://github.com/vllm-project/vllm/issues/15554) |
| 状态 | closed |
| 标签 | bug;stale;v1 |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug][V1]: ngram + guided decoding

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug when running `VLLM_USE_V1=1 vllm serve stelterlab/Mistral-Small-24B-Instruct-2501-AWQ --tensor-parallel-size 2 --gpu-memory-utilization 0.7 --guided-decoding-backend auto --speculative-model [ngram] --num-speculative-tokens 3` using v0.8.2 some decodings will fail with following error: ``` Warning: Parser Error: token " null" doesn't satisfy the grammar; byte 'n' fails parse; stopping WARNING 03-26 15:23:05 [backend_guidance.py:86] LLMatcher error: Parser Error: token " null" doesn't satisfy the grammar; byte 'n' fails parse ``` issue does not persist when removing speculative decoding json schema that is sent: ```python from pydantic import BaseModel, Field from typing import Literal class InteractionType(BaseModel): type: Literal[ "Example interaction type 1", "Example interaction type 2", "Example interaction type 3", ] explanation: str | None = Field( None, title="Interaction Explanation", description="very brief explanation (max one sentence/200 characters) why this interaction type was chosen.", max_length=200, ) trigger_sentence: str | None = Field( None, title="Trigger Sentence", description="The sentence from the transcr...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: speculative decoding json schema that is sent: ```python from pydantic import BaseModel, Field from typing import Literal class InteractionType(BaseModel): type: Literal[ "Example interaction type 1", "Example interacti...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: cribe the bug when running `VLLM_USE_V1=1 vllm serve stelterlab/Mistral-Small-24B-Instruct-2501-AWQ --tensor-parallel-size 2 --gpu-memory-utilization 0.7 --guided-decoding-backend auto --speculative-model [ngram] --num-...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: --tensor-parallel-size 2 --gpu-memory-utilization 0.7 --guided-decoding-backend auto --speculative-model [ngram] --num-speculative-tokens 3` using v0.8.2 some decodings will fail with following error: ``` Warning: Parse...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug][V1]: ngram + guided decoding bug;stale;v1 ### Your current environment ### 🐛 Describe the bug when running `VLLM_USE_V1=1 vllm serve stelterlab/Mistral-Small-24B-Instruct-2501-AWQ --tensor-parallel-size 2 --gpu-me...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: correctness ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;operator;quantization;sampling;triton build_error;nan_inf env_dependency Your current envir...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
