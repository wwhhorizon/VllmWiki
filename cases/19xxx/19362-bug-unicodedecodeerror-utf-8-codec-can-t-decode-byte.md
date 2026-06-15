# vllm-project/vllm#19362: [Bug]: UnicodeDecodeError: 'utf-8' codec can't decode byte

| 字段 | 值 |
| --- | --- |
| Issue | [#19362](https://github.com/vllm-project/vllm/issues/19362) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: UnicodeDecodeError: 'utf-8' codec can't decode byte

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm running Triton Inference Server using the following image: ```yaml image: "nvcr.io/nvidia/tritonserver:25.05-vllm-python-py3" ``` When attempting to serve the model `meta-llama/Llama-4-Scout-17B-16E`, I encounter the following error: ```bash (VllmWorkerProcess pid=469) ERROR 06-09 09:52:51 [multiproc_worker_utils.py:238] return lambda *args, **kwargs: self.run(grid=grid, warmup=False, *args, **kwargs) (VllmWorkerProcess pid=469) ERROR 06-09 09:52:51 [multiproc_worker_utils.py:238] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (VllmWorkerProcess pid=469) ERROR 06-09 09:52:51 [multiproc_worker_utils.py:238] File "/usr/local/lib/python3.12/dist-packages/triton/runtime/jit.py", line 607, in run (VllmWorkerProcess pid=469) ERROR 06-09 09:52:51 [multiproc_worker_utils.py:238] device = driver.active.get_current_device() (VllmWorkerProcess pid=469) ERROR 06-09 09:52:51 [multiproc_worker_utils.py:238] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (VllmWorkerProcess pid=469) ERROR 06-09 09:52:51 [multiproc_worker_utils.py:238] File "/usr/local/lib/python3.12/dist-packages/triton/runtime/driver.py", line 23, in __getattr__ (VllmWorkerProcess pi...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: pid=469) ERROR 06-09 09:52:51 [multiproc_worker_utils.py:238] mod = compile_module_from_src(Path(os.path.join(dirname, "driver.c")).read_text(), "cuda_utils") (VllmWorkerProcess pid=469) ERROR 06-09 09:52:51 [multiproc_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: 9) ERROR 06-09 09:52:51 [multiproc_worker_utils.py:238] self.utils = CudaUtils() # TODO: make static (VllmWorkerProcess pid=469) ERROR 06-09 09:52:51 [multiproc_worker_utils.py:238] ^^^^^^^^^^^ (VllmWorkerProcess pid=46...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: dia/tritonserver:25.05-vllm-python-py3" ``` When attempting to serve the model `meta-llama/Llama-4-Scout-17B-16E`, I encounter the following error: ```bash (VllmWorkerProcess pid=469) ERROR 06-09 09:52:51 [multiproc_wor...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: bug ### Your current environment ### 🐛 Describe the bug I'm running Triton Inference Server using the following image: ```yaml image: "nvcr.io/nvidia/tritonserver:25.05-vllm-python-py3" ``` When attempting to serve the...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: .py:238] return lambda *args, **kwargs: self.run(grid=grid, warmup=False, *args, **kwargs) (VllmWorkerProcess pid=469) ERROR 06-09 09:52:51 [multiproc_worker_utils.py:238] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
