# vllm-project/vllm#24959: [Bug]: vllm启动qwen3-32B-AWQ后进行对话报错

| 字段 | 值 |
| --- | --- |
| Issue | [#24959](https://github.com/vllm-project/vllm/issues/24959) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | cold_start |
| Operator 关键词 | attention;kernel;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm启动qwen3-32B-AWQ后进行对话报错

### Issue 正文摘录

### Your current environment vllm ：0.10.1.1 transformers ：4.56.1 启动命令 export CUDA_VISIBLE_DEVICES=0,1,2,3 && nohup vllm serve Qwen3-32B-AWQ \ --tensor-parallel-size 4 \ --dtype half \ --cpu-offload-gb 1 \ --gpu-memory-utilization 0.9 \ --host 0.0.0.0 \ --enable-auto-tool-choice \ --tool-call-parser hermes \ --port 10000 > qwen3-32B.log 2>&1 & disown && tail -fn 200 qwen3-32B.log ### 🐛 Describe the bug 当模型启动成功进行对话时，报错 error: Failures have been detected while processing an MLIR pass pipeline /root/miniconda3/envs/vllm/lib/python3.11/site-packages/vllm/attention/ops/prefix_prefill.py:36:0: note: Pipeline failed while executing [`ConvertTritonGPUToLLVM` on 'builtin.module' operation]: reproducer generated at `std::errs, please share the reproducer above with Triton project.` (APIServer pid=3176541) ERROR 09-16 10:40:29 [serving_chat.py:1051] Error in chat completion stream generator. (APIServer pid=3176541) ERROR 09-16 10:40:29 [serving_chat.py:1051] Traceback (most recent call last): (APIServer pid=3176541) ERROR 09-16 10:40:29 [serving_chat.py:1051] File "/root/miniconda3/envs/vllm/lib/python3.11/site-packages/vllm/entrypoints/openai/serving_chat.py", line 545, in chat_completion_st...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: line 569, in run ERROR 09-16 10:40:29 [engine.py:176] kernel = self.compile(src, target=target, options=options.__dict__) ERROR 09-16 10:40:29 [engine.py:176] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ E...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: ur current environment vllm ：0.10.1.1 transformers ：4.56.1 启动命令 export CUDA_VISIBLE_DEVICES=0,1,2,3 && nohup vllm serve Qwen3-32B-AWQ \ --tensor-parallel-size 4 \ --dtype half \ --cpu-offload-gb 1 \ --gpu-memory-utiliza...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: vllm启动qwen3-32B-AWQ后进行对话报错 bug;stale ### Your current environment vllm ：0.10.1.1 transformers ：4.56.1 启动命令 export CUDA_VISIBLE_DEVICES=0,1,2,3 && nohup vllm serve Qwen3-32B-AWQ \ --tensor-parallel-size 4 \ --dtyp...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: s/prefix_prefill.py:36:0: note: Pipeline failed while executing [`ConvertTritonGPUToLLVM` on 'builtin.module' operation]: reproducer generated at `std::errs, please share the reproducer above with Triton project.` (APIS...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: 0,1,2,3 && nohup vllm serve Qwen3-32B-AWQ \ --tensor-parallel-size 4 \ --dtype half \ --cpu-offload-gb 1 \ --gpu-memory-utilization 0.9 \ --host 0.0.0.0 \ --enable-auto-tool-choice \ --tool-call-parser hermes \ --port 1...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
