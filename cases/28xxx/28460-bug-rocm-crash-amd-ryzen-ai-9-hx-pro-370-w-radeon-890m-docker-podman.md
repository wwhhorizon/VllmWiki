# vllm-project/vllm#28460: [Bug]: rocm crash AMD Ryzen AI 9 HX PRO 370 w/ Radeon 890M - docker/podman

| 字段 | 值 |
| --- | --- |
| Issue | [#28460](https://github.com/vllm-project/vllm/issues/28460) |
| 状态 | closed |
| 标签 | bug;feature request;rocm;gpt-oss |
| 评论 | 20; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: rocm crash AMD Ryzen AI 9 HX PRO 370 w/ Radeon 890M - docker/podman

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Crashes when running rocm/vllm-dev:nightly to deploy `openai/gpt-oss-20b` on a AMD Ryzen AI 9 HX PRO 370 w/ Radeon 890M. Please see the stacktrace below ```` root@t0101841-arch:/app# vllm serve --model=openai/gpt-oss-20b --download-dir=/app/model/ WARNING 11-11 10:01:43 [argparse_utils.py:203] With `vllm serve`, you should provide the model as a positional argument or in a config file instead of via the `--model` option. The `--model` option will be removed in v0.13. (APIServer pid=13) INFO 11-11 10:01:43 [api_server.py:1963] vLLM API server version 0.11.1rc7.dev4+ga5a790eea (APIServer pid=13) INFO 11-11 10:01:43 [utils.py:253] non-default args: {'model_tag': 'openai/gpt-oss-20b', 'model': 'openai/gpt-oss-20b', 'download_dir': '/app/model/'} config.json: 1.81kB [00:00, 14.2MB/s] (APIServer pid=13) INFO 11-11 10:01:48 [model.py:630] Resolved architecture: GptOssForCausalLM model.safetensors.index.json: 36.4kB [00:00, 67.1MB/s] Parse safetensors files: 100%|█████████████████████████████████████████| 3/3 [00:00 , 'use_cudagraph': True, 'cudagraph_num_of_warmups': 1, 'cudagraph_capture_sizes': [1, 2, 4, 8, 16, 24, 32, 40, 48, 56, 64,...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: rocm crash AMD Ryzen AI 9 HX PRO 370 w/ Radeon 890M - docker/podman bug;feature request;rocm;gpt-oss ### Your current environment ### 🐛 Describe the bug Crashes when running rocm/vllm-dev:nightly to deploy `opena...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: Triton Attention backend. (EngineCore_DP0 pid=166) INFO 11-11 10:01:57 [mxfp4.py:150] Using Triton backend Loading safetensors checkpoint shards: 0% Completed | 0/3 [00:00 (APIServer pid=13) sys.exit(main()) (APIServer...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: -20b... (EngineCore_DP0 pid=166) INFO 11-11 10:01:57 [rocm.py:298] Using Triton Attention backend. (EngineCore_DP0 pid=166) INFO 11-11 10:01:57 [mxfp4.py:150] Using Triton backend Loading safetensors checkpoint shards:...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: rocm crash AMD Ryzen AI 9 HX PRO 370 w/ Radeon 890M - docker/podman bug;feature request;rocm;gpt-oss ### Your current environment ### 🐛 Describe the bug Crashes when running rocm/vllm-dev:nightly to deploy `opena...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: AI 9 HX PRO 370 w/ Radeon 890M - docker/podman bug;feature request;rocm;gpt-oss ### Your current environment ### 🐛 Describe the bug Crashes when running rocm/vllm-dev:nightly to deploy `openai/gpt-oss-20b` on a AMD Ryze...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
