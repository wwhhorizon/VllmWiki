# vllm-project/vllm#34941: [CI Failure]: Intel GPU Test :  examples/offline_inference/basic/generate.py

| 字段 | 值 |
| --- | --- |
| Issue | [#34941](https://github.com/vllm-project/vllm/issues/34941) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: Intel GPU Test :  examples/offline_inference/basic/generate.py

### Issue 正文摘录

### Name of failing test python3 examples/offline_inference/basic/generate.py --model facebook/opt-125m --block-size 64 --enforce-eager ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test buildkite link - https://buildkite.com/vllm/ci/builds/52218#019c74b4-5f21-4987-9119-bd0318acb010 python3 examples/offline_inference/basic/generate.py --model facebook/opt-125m --block-size 64 --enforce-eager fails with ``` INFO 02-19 07:12:10 [utils.py:229] non-default args: {'block_size': 64, 'enforce_eager': True, 'enable_lora': None, 'reasoning_parser_plugin': '', 'model': 'facebook/opt-125m'} INFO 02-19 07:12:22 [model.py:532] Resolved architecture: OPTForCausalLM INFO 02-19 07:12:22 [model.py:1556] Using max model len 2048 INFO 02-19 07:12:22 [scheduler.py:224] Chunked prefill is enabled with max_num_batched_tokens=8192. INFO 02-19 07:12:22 [vllm.py:697] Asynchronous scheduling is enabled. WARNING 02-19 07:12:22 [vllm.py:731] Enforce eager set, disabling torch.compile and CUDAGraphs. This is equivalent to setting -cc.mode=none -cc.cudagraph_mode=none WARNING 02-19 07:12:22 [vllm.py:...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [CI Failure]: Intel GPU Test : examples/offline_inference/basic/generate.py ci-failure ### Name of failing test python3 examples/offline_inference/basic/generate.py --model facebook/opt-125m --block-size 64 --enforce-ea
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: to, device_config=xpu, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser='', reasoning_parser_p...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: e=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=2048, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, data_parallel_size=1...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: examples/offline_inference/basic/generate.py --model facebook/opt-125m --block-size 64 --enforce-eager ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: of failing test python3 examples/offline_inference/basic/generate.py --model facebook/opt-125m --block-size 64 --enforce-eager ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
