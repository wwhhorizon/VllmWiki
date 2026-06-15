# vllm-project/vllm#35572: [Bug]: 在线跑GLM-5，开dp，遇到RuntimeError: Triton Error [CUDA]: an illegal memory access was encountered

| 字段 | 值 |
| --- | --- |
| Issue | [#35572](https://github.com/vllm-project/vllm/issues/35572) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support;moe;quantization |
| 子分类 | cold_start |
| Operator 关键词 | cuda;fp8;kernel;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: 在线跑GLM-5，开dp，遇到RuntimeError: Triton Error [CUDA]: an illegal memory access was encountered

### Issue 正文摘录

### Your current environment vllm版本：0.16.0 测试模型：GLM-5 机器：H100 运行代码： `vllm serve \ --trust-remote-code \ --data-parallel-size 8 \ --host \ --port \ --quantization fp8 \ --max-num-seqs 8 \ --max-model-len 65556 \ --gpu-memory-utilization 0.9 \ --no-enable-prefix-caching \ --no-enable-chunked-prefill \ --data-parallel-backend ray \ --compilation-config '{"cudagraph_mode":"NONE"}' ` ### 🐛 Describe the bug 开TP能正常起服务，开DP就会遇到下面问题 Traceback (most recent call last): File "/root/anaconda3/envs/vllm_0160/bin/vllm", line 6, in sys.exit(main()) File "/root/anaconda3/envs/vllm_0160/lib/python3.10/site-packages/vllm/entrypoints/cli/main.py", line 73, in main args.dispatch_function(args) File "/root/anaconda3/envs/vllm_0160/lib/python3.10/site-packages/vllm/entrypoints/cli/serve.py", line 108, in cmd run_multi_api_server(args) File "/root/anaconda3/envs/vllm_0160/lib/python3.10/site-packages/vllm/entrypoints/cli/serve.py", line 248, in run_multi_api_server with launch_core_engines( File "/root/anaconda3/envs/vllm_0160/lib/python3.10/contextlib.py", line 135, in __enter__ return next(self.gen) File "/root/anaconda3/envs/vllm_0160/lib/python3.10/site-packages/vllm/v1/engine/utils.py", line 850, in...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: -code \ --data-parallel-size 8 \ --host \ --port \ --quantization fp8 \ --max-num-seqs 8 \ --max-model-len 65556 \ --gpu-memory-utilization 0.9 \ --no-enable-prefix-caching \ --no-enable-chunked-prefill \ --data-paralle...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: 在线跑GLM-5，开dp，遇到RuntimeError: Triton Error [CUDA]: an illegal memory access was encountered bug;stale ### Your current environment vllm版本：0.16.0 测试模型：GLM-5 机器：H100 运行代码： `vllm serve \ --trust-remote-code \ --data-...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: vllm/compilation/decorators.py", line 559, in __call__ output = TorchCompileWithNoGuardsWrapper.__call__(self, *args, **kwargs) # type: ignore[arg-type] File "/root/anaconda3/envs/vllm_0160/lib/python3.10/site-packages/...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: 在线跑GLM-5，开dp，遇到RuntimeError: Triton Error [CUDA]: an illegal memory access was encountered bug;stale ### Your current environment vllm版本：0.16.0 测试模型：GLM-5 机器：H100 运行代码： `vllm serve \ --trust-remote-code \ --data-...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: site-packages/vllm/v1/engine/core.py", line 113, in __init__ num_gpu_blocks, num_cpu_blocks, kv_cache_config = self._initialize_kv_caches( File "/root/anaconda3/envs/vllm_0160/lib/python3.10/site-packages/vllm/v1/engine...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
