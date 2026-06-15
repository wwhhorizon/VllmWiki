# vllm-project/vllm#2641: Error: `resource already mapped` in `custom_all_reduce.cuh`

| 字段 | 值 |
| --- | --- |
| Issue | [#2641](https://github.com/vllm-project/vllm/issues/2641) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | distributed_parallel;model_support;quantization |
| 子分类 | runtime_err |
| Operator 关键词 | cuda;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> Error: `resource already mapped` in `custom_all_reduce.cuh`

### Issue 正文摘录

This is a issue relared to https://github.com/vllm-project/vllm/issues/2619#issuecomment-1913490065 I have tried `ray=2.9.1` with dev code in commit #2636 vllm.entrypoints.openai.api_server --model ./Mistral-7B-Instruct-v0.2-AWQ --quantization awq --dtype auto --host 0.0.0.0 --port 8081 --tensor-parallel-size 2 but I meet another error Failed: Cuda error /home/my/vllm/csrc/custom_all_reduce.cuh:417 'resource already mapped' Segmentation fault (core dumped) I am running with `python=3.11`, `CUDA 12.1`, `driver 530` with 2x RTX 3090 NVLink. When I rollback to commit #2622, the program works well. So it seems it is caused by #2192

## 现有链接修复摘要

#2192 Custom all reduce kernels | #2622 Use head_dim in config if exists

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: running with `python=3.11`, `CUDA 12.1`, `driver 530` with 2x RTX 3090 NVLink. When I rollback to commit #2622, the program works well. So it seems it is caused by #2192 development distributed_parallel;model_support;qu...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: m.entrypoints.openai.api_server --model ./Mistral-7B-Instruct-v0.2-AWQ --quantization awq --dtype auto --host 0.0.0.0 --port 8081 --tensor-parallel-size 2 but I meet another error Failed: Cuda error /home/my/vllm/csrc/c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: .0 --port 8081 --tensor-parallel-size 2 but I meet another error Failed: Cuda error /home/my/vllm/csrc/custom_all_reduce.cuh:417 'resource already mapped' Segmentation fault (core dumped) I am running with `python=3.11`...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: .1` with dev code in commit #2636 vllm.entrypoints.openai.api_server --model ./Mistral-7B-Instruct-v0.2-AWQ --quantization awq --dtype auto --host 0.0.0.0 --port 8081 --tensor-parallel-size 2 but I meet another error Fa...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#2192](https://github.com/vllm-project/vllm/pull/2192) | mentioned | 0.45 | Custom all reduce kernels | to commit #2622, the program works well. so it seems it is caused by #2192 bug |
| [#2622](https://github.com/vllm-project/vllm/pull/2622) | mentioned | 0.45 | Use head_dim in config if exists | .1`, `driver 530` with 2x rtx 3090 nvlink. when i rollback to commit #2622, the program works well. so it seems it is caused by #2192 bug |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
