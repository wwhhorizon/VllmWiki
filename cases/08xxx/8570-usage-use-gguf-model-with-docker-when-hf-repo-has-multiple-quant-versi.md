# vllm-project/vllm#8570: [Usage]: Use GGUF model with docker when hf repo has multiple quant versions

| 字段 | 值 |
| --- | --- |
| Issue | [#8570](https://github.com/vllm-project/vllm/issues/8570) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;frontend_api;model_support;quantization |
| 子分类 | memory |
| Operator 关键词 | cuda;quantization |
| 症状 | oom |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Use GGUF model with docker when hf repo has multiple quant versions

### Issue 正文摘录

### Update: I posted the solution below in my next comment. ### Your current environment I skipped the collect_env step as I use the latest docker container `v0.6.1.post2` of vllm. ### How would you like to use vllm I want to use a GGUF variant of the [Mistral Large Instruct 2407](https://huggingface.co/mistralai/Mistral-Large-Instruct-2407) model with vllm inside a docker container. I followed [the docs](https://docs.vllm.ai/en/latest/serving/deploying_with_docker.html) for setting up a container. The repos listed under the [quantized category](https://huggingface.co/models?other=base_model:quantized:mistralai/Mistral-Large-Instruct-2407) of the model are all GGUF, each with multiple different quant versions inside them. Only 2 of the repos have a `config.json` ([this](https://huggingface.co/gaianet/Mistral-Large-Instruct-2407-GGUF/tree/main) and [this](https://huggingface.co/second-state/Mistral-Large-Instruct-2407-GGUF/tree/main)). How can I tell vllm which quantized version of a repo I want to use? Info: I use an A100 80GB. What I tried: > docker run --gpus all --name vllm -v /mnt/disk1/hf_models:/root/.cache/huggingface --env "HUGGING_FACE_HUB_TOKEN= " -p 8080:8000 --ipc=host...

## 现有链接修复摘要

#8618 [Doc] Add documentation for GGUF quantization

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Usage]: Use GGUF model with docker when hf repo has multiple quant versions usage ### Update: I posted the solution below in my next comment. ### Your current environment I skipped the collect_env step as I use the lat...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Usage]: Use GGUF model with docker when hf repo has multiple quant versions usage ### Update: I posted the solution below in my next comment. ### Your current environment I skipped the collect_env step as I use the lat...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ll vllm which quantized version of a repo I want to use? Info: I use an A100 80GB. What I tried: > docker run --gpus all --name vllm -v /mnt/disk1/hf_models:/root/.cache/huggingface --env "HUGGING_FACE_HUB_TOKEN= " -p 8...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Usage]: Use GGUF model with docker when hf repo has multiple quant versions usage ### Update: I posted the solution below in my next comment. ### Your current environment I skipped the collect_env step as I use the lat...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: mance ci_build;frontend_api;model_support;quantization cuda;quantization oom env_dependency #8618 [Doc] Add documentation for GGUF quantization Update: I posted the solution below in my next comment.

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#8618](https://github.com/vllm-project/vllm/pull/8618) | closes_keyword | 0.95 | [Doc] Add documentation for GGUF quantization | resolve*) This PR adds GGUF quantization documents for some frequently asked basic usage issues like: - #8570 - #8401 - #7978 **BEFORE SUBMITTING, PLEASE READ THE CHECKL |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
