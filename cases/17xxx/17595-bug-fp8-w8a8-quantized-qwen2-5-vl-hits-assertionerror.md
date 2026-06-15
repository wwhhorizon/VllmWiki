# vllm-project/vllm#17595: [Bug]: fp8 w8a8 quantized Qwen2.5-VL hits AssertionError

| 字段 | 值 |
| --- | --- |
| Issue | [#17595](https://github.com/vllm-project/vllm/issues/17595) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | gemm_linear;quantization |
| 子分类 |  |
| Operator 关键词 | fp8;operator;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: fp8 w8a8 quantized Qwen2.5-VL hits AssertionError

### Issue 正文摘录

### Your current environment vLLM v0.8.4 on Tesla L40S. ### 🐛 Describe the bug See also these closed issues: #7550 #15264 ``` ERROR 05-02 09:48:39 [engine.py:160] AssertionError() ERROR 05-02 09:48:39 [engine.py:160] Traceback (most recent call last): ERROR 05-02 09:48:39 [engine.py:160] File "/usr/local/lib/python3.12/dist-packages/vllm/engine/multiprocessing/engine.py", line 158, in start ERROR 05-02 09:48:39 [engine.py:160] self.run_engine_loop() ERROR 05-02 09:48:39 [engine.py:160] File "/usr/local/lib/python3.12/dist-packages/vllm/engine/multiprocessing/engine.py", line 221, in run_engine_loop ERROR 05-02 09:48:39 [engine.py:160] request_outputs = self.engine_step() ERROR 05-02 09:48:39 [engine.py:160] ^^^^^^^^^^^^^^^^^^ ERROR 05-02 09:48:39 [engine.py:160] File "/usr/local/lib/python3.12/dist-packages/vllm/engine/multiprocessing/engine.py", line 247, in engine_step ERROR 05-02 09:48:39 [engine.py:160] raise e ERROR 05-02 09:48:39 [engine.py:160] File "/usr/local/lib/python3.12/dist-packages/vllm/engine/multiprocessing/engine.py", line 230, in engine_step ERROR 05-02 09:48:39 [engine.py:160] return self.engine.step() ERROR 05-02 09:48:39 [engine.py:160] ^^^^^^^^^^^^^^^^^^ ERR...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: fp8 w8a8 quantized Qwen2.5-VL hits AssertionError bug;stale ### Your current environment vLLM v0.8.4 on Tesla L40S. ### 🐛 Describe the bug See also these closed issues: #7550 #15264 ``` ERROR 05-02 09:48:39 [engi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: fp8 w8a8 quantized Qwen2.5-VL hits AssertionError bug;stale ### Your current environment vLLM v0.8.4 on Tesla L40S. ### 🐛 Describe the bug See also these closed issues: #7550 #15264 ``` ERROR 05-02 09:48:39 [engi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: fp8 w8a8 quantized Qwen2.5-VL hits AssertionError bug;stale ### Your current environment vLLM v0.8.4 on Tesla L40S. ### 🐛 Describe the bug See also these closed issues: #7550 #15264 ``` ERROR 05-02 09:48:39 [engi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: line 200, in apply ERROR 05-02 09:48:39 [engine.py:160] output = ops.cutlass_scaled_mm(qinput, ERROR 05-02 09:48:39 [engine.py:160] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 05-02 09:48:39 [engine.py:160] File "/usr/local/lib...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: pment gemm_linear;quantization fp8;operator;quantization crash dtype;env_dependency;shape Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
