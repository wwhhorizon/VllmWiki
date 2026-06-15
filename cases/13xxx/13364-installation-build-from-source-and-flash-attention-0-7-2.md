# vllm-project/vllm#13364: [Installation]: Build from source and flash-attention (0.7.2)

| 字段 | 值 |
| --- | --- |
| Issue | [#13364](https://github.com/vllm-project/vllm/issues/13364) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build |
| 子分类 | install |
| Operator 关键词 | attention;cuda |
| 症状 | build_error |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: Build from source and flash-attention (0.7.2)

### Issue 正文摘录

### Your current environment isolated system, can't provide environment. ### How you are installing vllm pip install . Is install from source using VLLM_FLASH_ATTN_SRC_DIR still supported? I don't see it documented in the https://docs.vllm.ai/en/latest/getting_started/installation/gpu/index.html#build-wheel-from-source? Does the vLLM build build flash-attention or just copy stuff over. There seem to be an issue with a missing target for "_vllm_fa2_C" in the build/temp* directory. If not, is there any trick to build flash-attention separately and incorporate it into an installation of vllm built from scratch. (I have an isolated machine with old CUDA that I'm trying to build a version of vLLM for) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Installation]: Build from source and flash-attention (0.7.2) installation ### Your current environment isolated system, can't provide environment. ### How you are installing vllm pip install . Is install from source
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: lation of vllm built from scratch. (I have an isolated machine with old CUDA that I'm trying to build a version of vLLM for) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues,...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: l supported? I don't see it documented in the https://docs.vllm.ai/en/latest/getting_started/installation/gpu/index.html#build-wheel-from-source? Does the vLLM build build flash-attention or just copy stuff over. There...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
