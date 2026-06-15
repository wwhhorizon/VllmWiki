# vllm-project/vllm#21562: [Bug]: [DP/EP] DeepGEMM with Qwen Fails

| 字段 | 值 |
| --- | --- |
| Issue | [#21562](https://github.com/vllm-project/vllm/issues/21562) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: [DP/EP] DeepGEMM with Qwen Fails

### Issue 正文摘录

``` containers: - name: vllm image: "quay.io/wseaton/vllm:llmd-multistage-6" imagePullPolicy: Always args: - "--model" - "RedHatAI/Llama-4-Scout-17B-16E-Instruct-FP8-dynamic" - "--tensor-parallel-size" - "4" - "--max-model-len" - "32000" - "--disable-log-requests" ``` ``` (EngineCore_3 pid=103) ERROR 07-25 02:51:33 [core.py:592] File "/tmp/vllm-8dfb45ca3379b3a789ec529af4bf725daa07f10d/vllm/compilation/cuda_piecewise_backend.py", line 112, in __call__ (EngineCore_3 pid=103) ERROR 07-25 02:51:33 [core.py:592] return self.compiled_graph_for_general_shape(*args) (EngineCore_3 pid=103) ERROR 07-25 02:51:33 [core.py:592] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_3 pid=103) ERROR 07-25 02:51:33 [core.py:592] File "/opt/vllm/lib64/python3.12/site-packages/torch/_dynamo/eval_frame.py", line 838, in _fn (EngineCore_3 pid=103) ERROR 07-25 02:51:33 [core.py:592] return fn(*args, **kwargs) (EngineCore_3 pid=103) ERROR 07-25 02:51:33 [core.py:592] ^^^^^^^^^^^^^^^^^^^ (EngineCore_3 pid=103) ERROR 07-25 02:51:33 [core.py:592] File "/opt/vllm/lib64/python3.12/site-packages/torch/_functorch/aot_autograd.py", line 1209, in forward (EngineCore_3 pid=103) ERROR 07-25 02:51:33 [core.py:5...

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 6: [Bug]: [DP/EP] DeepGEMM with Qwen Fails bug ``` containers: - name: vllm image: "quay.io/wseaton/vllm:llmd-multistage-6" imagePullPolicy: Always args: - "--model" - "RedHatAI/
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: [DP/EP] DeepGEMM with Qwen Fails bug ``` containers: - name: vllm image: "quay.io/wseaton/vllm:llmd-multistage-6" imagePullPolicy: Always args: - "--model" - "RedHatAI/Llama-4-Sc
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: - "--model" - "RedHatAI/Llama-4-Scout-17B-16E-Instruct-FP8-dynamic" - "--tensor-parallel-size" - "4" - "--max-model-len" - "32000" - "--disable-log-requests" ``` ``` (EngineCore_3 pid=103) ERROR 07-25 02:51:33 [core.py:...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: .py:592] return lambda *args, **kwargs: self.run(grid=grid, warmup=False, *args, **kwargs) (EngineCore_3 pid=103) ERROR 07-25 02:51:33 [core.py:592] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_3 pid=1...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: 8dfb45ca3379b3a789ec529af4bf725daa07f10d/vllm/compilation/cuda_piecewise_backend.py", line 112, in __call__ (EngineCore_3 pid=103) ERROR 07-25 02:51:33 [core.py:592] return self.compiled_graph_for_general_shape(*args) (...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
