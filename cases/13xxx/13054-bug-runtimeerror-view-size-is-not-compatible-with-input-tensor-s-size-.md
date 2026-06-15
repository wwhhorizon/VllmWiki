# vllm-project/vllm#13054: [Bug]: RuntimeError: view size is not compatible with input tensor's size and stride (at least one dimension spans across two contiguous subspaces). Use .reshape(...) instead. on Gaudi2

| 字段 | 值 |
| --- | --- |
| Issue | [#13054](https://github.com/vllm-project/vllm/issues/13054) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RuntimeError: view size is not compatible with input tensor's size and stride (at least one dimension spans across two contiguous subspaces). Use .reshape(...) instead. on Gaudi2

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Build vLLM using: ``` docker build -t vllm-hpu:v0.7.2-mainline -f Dockerfile.hpu . ``` Then run it using: ``` "cd /workspace/vllm && pip install git+https://github.com/huggingface/transformers accelerate && pip install qwen-vl-utils[decord]==0.0.8 && vllm serve Qwen/Qwen2.5-VL-7B-Instruct --disable_log_requests --port 8080 --tensor-parallel-size 2" ``` The hardware is a node with 8 Gaudi 2 HL-225H mezzanine cards with 2x Xeon 8380 Processors. The container has 2 Gaudi 2 cards, 70Gi memory and 25Gi of hugepages-2Mi assigned to it. ```text view size is not compatible with input tensor's size and stride (at least one dimension spans across two contiguous subspaces). Use .reshape(...) instead. Traceback (most recent call last): File "/usr/local/lib/python3.10/dist-packages/vllm-0.7.2+gaudi000-py3.10.egg/vllm/engine/multiprocessing/engine.py", line 380, in run_mp_engine engine = MQLLMEngine.from_engine_args(engine_args=engine_args, File "/usr/local/lib/python3.10/dist-packages/vllm-0.7.2+gaudi000-py3.10.egg/vllm/engine/multiprocessing/engine.py", line 123, in from_engine_args return cls(ipc_path=ipc_path, File "/usr/local/lib/python3....

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: audi2 bug;stale ### Your current environment ### 🐛 Describe the bug Build vLLM using: ``` docker build -t vllm-hpu:v0.7.2-mainline -f Dockerfile.hpu . ``` Then run it using: ``` "cd /workspace/vllm && pip install git+ht...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: it using: ``` "cd /workspace/vllm && pip install git+https://github.com/huggingface/transformers accelerate && pip install qwen-vl-utils[decord]==0.0.8 && vllm serve Qwen/Qwen2.5-VL-7B-Instruct --disable_log_requests --...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: : RuntimeError: view size is not compatible with input tensor's size and stride (at least one dimension spans across two contiguous subspaces). Use .reshape(...) instead. on Gaudi2 bug;stale ### Your current environment...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ross two contiguous subspaces). Use .reshape(...) instead. on Gaudi2 bug;stale ### Your current environment ### 🐛 Describe the bug Build vLLM using: ``` docker build -t vllm-hpu:v0.7.2-mainline -f Dockerfile.hpu . ``` T...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: m-0.7.2+gaudi000-py3.10.egg/vllm/scripts.py", line 204, in main args.dispatch_function(args) File "/usr/local/lib/python3.10/dist-packages/vllm-0.7.2+gaudi000-py3.10.egg/vllm/scripts.py", line 44, in serve uvloop.run(ru...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
