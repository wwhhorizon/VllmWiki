# vllm-project/vllm#18727: [Bug]: OpenAI Classification Client returning logits instead of softmax values

| 字段 | 值 |
| --- | --- |
| Issue | [#18727](https://github.com/vllm-project/vllm/issues/18727) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: OpenAI Classification Client returning logits instead of softmax values

### Issue 正文摘录

### 🐛 Describe the bug After installing `0.9.0` pre-release from the following wheel https://wheels.vllm.ai/c533c6fa8403f8bb3a75f130e063dbaafc1d69dc/vllm-0.9.0-cp38-abi3-manylinux1_x86_64.whl, I see that for `papluca/xlm-roberta-base-language-detection` model raw logits are being returned instead of softmax output. #### Steps to reproduce ``` pip install https://wheels.vllm.ai/c533c6fa8403f8bb3a75f130e063dbaafc1d69dc/vllm-0.9.0-cp38-abi3-manylinux1_x86_64.whl vllm serve 'papluca/xlm-roberta-base-language-detection' --port 8098 --host 0.0.0.0 --task classify ``` #### Wrong output When calling the model, I see raw logits being returned: ``` curl -v "http://127.0.0.1:8098/classify" \ -H "Content-Type: application/json" \ -d '{ "model": "papluca/xlm-roberta-base-language-detection", "input": "Hello" }' ``` Returns: ```json { "id": "classify-5b23c5f8efa24ccfb1ca60f6b4283006", "object": "list", "created": 1748283054, "model": "papluca/xlm-roberta-base-language-detection", "data": [ { "index": 0, "label": "en", "probs": [ -1.0625, 0.290771484375, -1.125, -0.9794921875, -0.339111328125, -0.1148681640625, -0.75439453125, 0.360107421875, -0.479736328125, 1.2421875, -0.338623046875, 0.671875...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: rning logits instead of softmax values bug ### 🐛 Describe the bug After installing `0.9.0` pre-release from the following wheel https://wheels.vllm.ai/c533c6fa8403f8bb3a75f130e063dbaafc1d69dc/vllm-0.9.0-cp38-abi3-manyli...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: raw logits are being returned instead of softmax output. #### Steps to reproduce ``` pip install https://wheels.vllm.ai/c533c6fa8403f8bb3a75f130e063dbaafc1d69dc/vllm-0.9.0-cp38-abi3-manylinux1_x86_64.whl vllm serve 'pap...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: llel;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;mismatch;nan_inf env_dependency <details>
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: x86_64.whl, I see that for `papluca/xlm-roberta-base-language-detection` model raw logits are being returned instead of softmax output. #### Steps to reproduce ``` pip install https://wheels.vllm.ai/c533c6fa8403f8bb3a75...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;mismatch;nan_inf env_dependency <details>

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
