# vllm-project/vllm#9360: [Bug]: Error running Molmo on API in v0.6.3

| 字段 | 值 |
| --- | --- |
| Issue | [#9360](https://github.com/vllm-project/vllm/issues/9360) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Error running Molmo on API in v0.6.3

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Attempting to run the new Molmo-7B-D-0924 model through vLLM failed and produced an error - Steps to reproduce: ``` conda create -n vLLM2 python=3.11 conda activate vLLM2 pip install vllm vllm serve ./Molmo-7B-D-0924/ --trust-remote-code ``` and (edited from an example in the documentation) ``` curl http://0.0.0.0:8000/v1/completions \ -H "Content-Type: application/json" \ -d '{ "model": "./Molmo-7B-D-0924/", "prompt": "San Francisco is a", "max_tokens": 7, "temperature": 0 }' ``` returned ``` Internal Server Error(base) ``` with the Molmo model folder, a local copy as downloaded from https://huggingface.co/allenai/Molmo-7B-D-0924 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#9397 [Bugfix] Molmo text-only input bug fix

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: eproduce: ``` conda create -n vLLM2 python=3.11 conda activate vLLM2 pip install vllm vllm serve ./Molmo-7B-D-0924/ --trust-remote-code ``` and (edited from an example in the documentation) ``` curl http://0.0.0.0:8000/...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 4 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whic...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: running Molmo on API in v0.6.3 bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Attempting to run the new Molmo-7B-D-0924 model through vLLM failed and produced an error - Step...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: upport;sampling_logits;speculative_decoding cache;cuda;operator;sampling;triton build_error;crash;nan_inf;slowdown env_dependency #9397 [Bugfix] Molmo text-only input bug fix Your current environment
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: lmo-7B-D-0924 model through vLLM failed and produced an error - Steps to reproduce: ``` conda create -n vLLM2 python=3.11 conda activate vLLM2 pip install vllm vllm serve ./Molmo-7B-D-0924/ --trust-remote-code ``` and (...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#9397](https://github.com/vllm-project/vllm/pull/9397) | closes_keyword | 0.95 | [Bugfix] Molmo text-only input bug fix | FIX #9360 --- <details> <!-- inside this <details> section, markdown rendering does not work, so we use raw html here. --> <summary><b> PR Checklist (Click to Expand) </b>< |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
