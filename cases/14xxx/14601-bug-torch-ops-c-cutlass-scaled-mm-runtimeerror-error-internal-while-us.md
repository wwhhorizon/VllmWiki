# vllm-project/vllm#14601: [Bug]: torch.ops._C.cutlass_scaled_mm RuntimeError: Error Internal while use L20 PP=3 + TP=8 for R1

| 字段 | 值 |
| --- | --- |
| Issue | [#14601](https://github.com/vllm-project/vllm/issues/14601) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization |
| 子分类 | cold_start |
| Operator 关键词 | attention;cuda;fp8;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: torch.ops._C.cutlass_scaled_mm RuntimeError: Error Internal while use L20 PP=3 + TP=8 for R1

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug - cmd: ```bash nohup python3 -m vllm.entrypoints.openai.api_server \ --model=/workspace/dev/hf_models/DeepSeek-R1 \ --dtype=auto \ --max-model-len 32768 \ --tensor-parallel-size 8 \ --pipeline-parallel-size 3 \ --tokenizer-mode auto \ --gpu-memory-utilization 0.90 \ --max-num-seqs 48 \ --trust-remote-code \ --no-enable-prefix-caching \ --enable-chunked-prefill=False \ --enforce-eager \ --disable-custom-all-reduce \ --port 8862 > vllm.R1.log.1 2>&1 & ``` - Error: ```bash Loading safetensors checkpoint shards: 96% Completed | 157/163 [01:22 [rank0]: uvloop.run(run_server(args)) [rank0]: File "/root/anaconda3/envs/trtllm/lib/python3.10/site-packages/uvloop/__init__.py", line 82, in run [rank0]: return loop.run_until_complete(wrapper()) [rank0]: File "uvloop/loop.pyx", line 1517, in uvloop.loop.Loop.run_until_complete [rank0]: File "/root/anaconda3/envs/trtllm/lib/python3.10/site-packages/uvloop/__init__.py", line 61, in wrapper [rank0]: return await main [rank0]: File "/root/anaconda3/envs/trtllm/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 947, in run_server [rank0]: async with build_async_engine_client...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Bug]: torch.ops._C.cutlass_scaled_mm RuntimeError: Error Internal while use L20 PP=3 + TP=8 for R1 bug ### Your current environment ### 🐛 Describe the bug - cmd: ```bash nohup python3 -m vllm.entrypoints.openai.api_ser...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: torch.ops._C.cutlass_scaled_mm RuntimeError: Error Internal while use L20 PP=3 + TP=8 for R1 bug ### Your current environment ### 🐛 Describe the bug - cmd: ```bash nohup python3 -m vllm.entrypoints.openai.api_ser...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: s/openai/api_server.py", line 947, in run_server [rank0]: async with build_async_engine_client(args) as engine_client: [rank0]: File "/root/anaconda3/envs/trtllm/lib/python3.10/contextlib.py", line 199, in __aenter__ [r...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ```bash nohup python3 -m vllm.entrypoints.openai.api_server \ --model=/workspace/dev/hf_models/DeepSeek-R1 \ --dtype=auto \ --max-model-len 32768 \ --tensor-parallel-size 8 \ --pipeline-parallel-size 3 \ --tokenizer-mod...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
