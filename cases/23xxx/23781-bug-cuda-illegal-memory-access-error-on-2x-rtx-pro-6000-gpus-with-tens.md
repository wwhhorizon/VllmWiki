# vllm-project/vllm#23781: [Bug]: CUDA illegal memory access error on 2x RTX PRO 6000 GPUs with --tensor-parallel-size=2

| 字段 | 值 |
| --- | --- |
| Issue | [#23781](https://github.com/vllm-project/vllm/issues/23781) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]: CUDA illegal memory access error on 2x RTX PRO 6000 GPUs with --tensor-parallel-size=2

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Please refer to the attached vllm logs. I am using two RTX PRO 6000 GPUs and attempting to run inference with both by setting `--tensor-parallel-size 2`. However, the process fails with an error. I am aware that similar issues have been reported in [previous posts](https://github.com/vllm-project/vllm/issues/13939), where the solution was to update to a newer version of vLLM. I am currently on the latest version, yet the problem persists. # Command(Docker) ``` docker run --name vllm-Qwen3 \ --runtime nvidia --gpus all \ -v ~/.cache/huggingface:/root/.cache/huggingface \ -p 8000:8000 \ vllm/vllm-openai:latest \ --model jart25/Qwen3-30B-A3B-Instruct-2507-Autoround-Int-4bit-gptq \ --tensor-parallel-size 2 \ --gpu-memory-utilization 0.5 ``` # vllm Logs https://gist.github.com/Cyp9715/e352bdd46b84a6aa7a490054354c55d3

## 现有链接修复摘要

#23942 [CI] Add `aiter` to matching list of issue auto labeller for `rocm` tag

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: -project/vllm/issues/13939), where the solution was to update to a newer version of vLLM. I am currently on the latest version, yet the problem persists. # Command(Docker) ``` docker run --name vllm-Qwen3 \ --runtime nv...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: CUDA illegal memory access error on 2x RTX PRO 6000 GPUs with --tensor-parallel-size=2 bug ### Your current environment ### 🐛 Describe the bug Please refer to the attached vllm logs. I am using two RTX PRO 6000 G...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: et the problem persists. # Command(Docker) ``` docker run --name vllm-Qwen3 \ --runtime nvidia --gpus all \ -v ~/.cache/huggingface:/root/.cache/huggingface \ -p 8000:8000 \ vllm/vllm-openai:latest \ --model jart25/Qwen...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: sampling_logits;speculative_decoding cuda;operator;quantization;sampling;triton build_error;nan_inf env_dependency #23942 [CI] Add `aiter` to matching list of issue auto labeller for `rocm` tag Your current environment
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: correctness ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;operator;quantization;sampling;triton build_error;nan_inf env_dependency #23942 [CI] Add `a...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#23942](https://github.com/vllm-project/vllm/pull/23942) | mentioned | 0.6 | [CI]  Add `aiter` to matching list of issue auto labeller for `rocm` tag | ches) • aiter (substring) in title: 1 matches (searchIn: title) #23781: Should have ROCm label: NO (0 matches) #23780: Should have ROCm label: NO (0 matches) #23776: Should hav |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
