# vllm-project/vllm#17410: [Bug]: GPTQ cannot be used on ROCm after upgraded vLLM to v0.8.5

| 字段 | 值 |
| --- | --- |
| Issue | [#17410](https://github.com/vllm-project/vllm/issues/17410) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: GPTQ cannot be used on ROCm after upgraded vLLM to v0.8.5

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I have been using GPTQ quantization on the ROCm platform, and I created an API server using the simple `vllm serve` command, which worked perfectly. However, after updating vLLM to version v0.8.5, the `vllm serve` command failed to start, showing the error message: "gptq_bitblas quantization is currently not supported in rocm." After manually adding the `--quantization gptq` parameter, vLLM worked normally as it did before. It should be noted that the GPU I am using is very old and no longer supported. Therefore, the vLLM I am using is a downstream branch that I maintain myself. However, I believe this issue also exists in the upstream branch here, so I am submitting this issue here. Below is the full log output: ```text (vllm085) nlzy@Nlzy-Lorazepam-100 ~/vllm ((ec44935b))> vllm serve /mnt/Qwen2.5-7B-Instruct-GPTQ-Int4/ INFO 04-29 19:56:35 [__init__.py:239] Automatically detected platform rocm. INFO 04-29 19:56:44 [api_server.py:1043] vLLM API server version 0.8.6.dev22+gec44935b0 INFO 04-29 19:56:44 [api_server.py:1044] args: Namespace(subparser='serve', model_tag='/mnt/Qwen2.5-7B-Instruct-GPTQ-Int4/', config='', host=None, por...

## 现有链接修复摘要

#17411 [Bugfix] Temporarily disable gptq_bitblas on ROCm

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: t (vllm085) nlzy@Nlzy-Lorazepam-100 ~/vllm ((ec44935b))> vllm serve /mnt/Qwen2.5-7B-Instruct-GPTQ-Int4/ INFO 04-29 19:56:35 [__init__.py:239] Automatically detected platform rocm. INFO 04-29 19:56:44 [api_server.py:1043...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: erve` command, which worked perfectly. However, after updating vLLM to version v0.8.5, the `vllm serve` command failed to start, showing the error message: "gptq_bitblas quantization is currently not supported in rocm."...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: r current environment ### 🐛 Describe the bug I have been using GPTQ quantization on the ROCm platform, and I created an API server using the simple `vllm serve` command, which worked perfectly. However, after updating v...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: okens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, tool_call_parser=None, tool_parser_plugin='', model='/mnt/Qwen2.5-7B-Instruct-GPTQ-Int4/'...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: True, config_format= , dtype='auto', max_model_len=None, guided_decoding_backend='auto', reasoning_parser=None, logits_processor_pattern=None, model_impl='auto', distributed_executor_backend=None, pipeline_parallel_size...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#17411](https://github.com/vllm-project/vllm/pull/17411) | closes_keyword | 0.95 | [Bugfix] Temporarily disable gptq_bitblas on ROCm | FIX #17410 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
