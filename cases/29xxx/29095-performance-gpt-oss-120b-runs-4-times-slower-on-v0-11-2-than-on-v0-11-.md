# vllm-project/vllm#29095: [Performance]: gpt-oss-120b runs 4 times slower on v0.11.2 than on v0.11.0

| 字段 | 值 |
| --- | --- |
| Issue | [#29095](https://github.com/vllm-project/vllm/issues/29095) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | cuda |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: gpt-oss-120b runs 4 times slower on v0.11.2 than on v0.11.0

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression I have been experimenting with running `gpt-oss-120b` ob 4xh100 with the latest versions of vLLM and I have noticed that after vLLM moved from v0.11.0 the performance dropped significantly, roughly by 4 times. I wonder if anyone else noticed that or if it is a local issue on my side. To reproduce, set a model path: ``` export MODEL_PATH=... ``` set a tag: ``` export VLLM_TAG=v0.11.0 ``` or ``` export VLLM_TAG=v0.11.2 ``` and run the server: ``` docker run \ -it --rm \ --shm-size 16G \ --network host \ --group-add video \ --security-opt seccomp=unconfined \ --security-opt apparmor=unconfined \ --cap-add=SYS_PTRACE \ --gpus '"device=all"' \ -v $MODEL_PATH:$MODEL_PATH \ vllm/vllm-openai:$VLLM_TAG \ --async-scheduling \ --no-enable-prefix-caching \ --model $MODEL_PATH \ --tensor-parallel-size 4 \ --max-num-seqs 64 \ --max-num-batched-tokens 23161 \ --max-model-len 10240 \ --cuda-graph-sizes 2048 \ --compilation-config '{"cudagraph_mode":"PIECEWISE"}' \ --port 8000 ``` Get the client (that is the one used here: https://inferencemax.semianalysis.com): ``` git clone https://github.com/kimbochen/bench_s...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 6: roposal to improve performance _No response_ ### Report of performance regression I have been experimenting with running `gpt-oss-120b` ob 4xh100 with the latest versions of vLLM and I have noticed that after vLLM moved...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: been experimenting with running `gpt-oss-120b` ob 4xh100 with the latest versions of vLLM and I have noticed that after vLLM moved from v0.11.0 the performance dropped significantly, roughly by 4 times. I wonder if anyo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: e regression I have been experimenting with running `gpt-oss-120b` ob 4xh100 with the latest versions of vLLM and I have noticed that after vLLM moved from v0.11.0 the performance dropped significantly, roughly by 4 tim...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Performance]: gpt-oss-120b runs 4 times slower on v0.11.2 than on v0.11.0 performance ### Proposal to improve performance _No response_ ### Report of performance regression I have been experimenting with running `gpt-o...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: dom-range-ratio=0.8 \ --num-prompts=640 \ --max-concurrency=64 \ --request-rate=inf \ --ignore-eos \ --percentile-metrics='ttft,tpot,itl,e2el' ``` For `v0.11.0` the result is something like: ============ Serving Benchma...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
