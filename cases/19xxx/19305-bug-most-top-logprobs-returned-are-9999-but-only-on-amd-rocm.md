# vllm-project/vllm#19305: [Bug]: Most top_logprobs returned are -9999, but only on amd/rocm.

| 字段 | 值 |
| --- | --- |
| Issue | [#19305](https://github.com/vllm-project/vllm/issues/19305) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Most top_logprobs returned are -9999, but only on amd/rocm.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm getting -9999 logprobs values for all tokens returned by token_logprobs, except for the first one or two, which typically have near to 0 logprob. The -9999 prob tail are all incoherent continuations / unused tokens. Note I'm running with temp=1, no other sampling params. This issue is only occurring on the AMD MI210 machine I'm testing on. No such issues on Nvidia gpus. Here's what the output looks like for the AMD machine: ``` {"id":"cmpl-099e6e05a54947bc815ebf68059a8c10","object":"text_completion","created":1749257509,"model":"google/gemma-3-4b-it","choices":[{"index":0,"text":"Princess","logprobs":{"text_offset":[0],"token_logprobs":[0.0],"tokens":["Princess"],"top_logprobs":[{"Princess":0.0,"":-9999.0," ":-9999.0," ":-9999.0,"[multimodal]":-9999.0," ":-9999.0," ":-9999.0," ":-9999.0," ":-9999.0," ":-9999.0," ":-9999.0," ":-9999.0," ":-9999.0," ":-9999.0," ":-9999.0," ":-9999.0," ":-9999.0," ":-9999.0}]},"finish_reason":"length","stop_reason":null,"prompt_logprobs":null}],"usage":{"prompt_tokens":10,"total_tokens":11,"completion_tokens":1,"prompt_tokens_details":null},"kv_transfer_params":null} ``` And from nvidia gpu: ```...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: 4947bc815ebf68059a8c10","object":"text_completion","created":1749257509,"model":"google/gemma-3-4b-it","choices":[{"index":0,"text":"Princess","logprobs":{"text_offset":[0],"token_logprobs":[0.0],"tokens":["Princess"],"...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: on_tokens":1,"prompt_tokens_details":null}} ``` Minimal repro steps: # install vllm: ``` # Install vLLM pip install --upgrade amdsmi sudo apt install -y build-essential ninja-build pkg-config pip install --upgrade "cmak...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: Most top_logprobs returned are -9999, but only on amd/rocm. bug;stale ### Your current environment ### 🐛 Describe the bug I'm getting -9999 logprobs values for all tokens returned by token_logprobs, except for th...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: --served-model-name google/gemma-3-4b-it --gpu-memory-utilization 0.95 --dtype bfloat16 --api-key xxx` # run inference: ``` curl http://localhost:8888/v1/completions \ -H "Authorization: Bearer xxx" \ -H "Content-Type:...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: # 5-10 min full compile ``` # run model: `vllm serve unsloth/gemma-3-4b-it --port 8888 --trust-remote-code --max-model-len 2500 --served-model-name google/gemma-3-4b-it --gpu-memory-utilization 0.95 --dtype bfloat16 --a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
