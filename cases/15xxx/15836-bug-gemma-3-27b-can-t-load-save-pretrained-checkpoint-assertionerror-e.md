# vllm-project/vllm#15836: [Bug]: Gemma-3 (27B) can't load save_pretrained() checkpoint: AssertionError: expected size 5376==2560, stride 1==1 at dim=0

| 字段 | 值 |
| --- | --- |
| Issue | [#15836](https://github.com/vllm-project/vllm/issues/15836) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 21; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Gemma-3 (27B) can't load save_pretrained() checkpoint: AssertionError: expected size 5376==2560, stride 1==1 at dim=0

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Reproduction code: ``` import os import torch from vllm import LLM from transformers import AutoTokenizer, AutoProcessor, Gemma3ForConditionalGeneration model_id = "google/gemma-3-27b-it" save_path = " " model = Gemma3ForConditionalGeneration.from_pretrained( model_id, torch_dtype=torch.bfloat16, device_map="cpu" ) tokenizer = AutoTokenizer.from_pretrained(model_id) processor = AutoProcessor.from_pretrained(model_id) if os.path.exists(save_path): import shutil shutil.rmtree(save_path) model.save_pretrained(save_path) tokenizer.save_pretrained(save_path) processor.save_pretrained(save_path) model = LLM( model=save_path, max_model_len=10240, tensor_parallel_size=8, limit_mm_per_prompt={"image": 5}, ) ``` ==== Error within `LLM()`: (VllmWorker rank=0 pid=75437) ERROR 03-31 15:54:20 [multiproc_executor.py:379] File "/home/agi/vllm/vllm/compilation/backends.py", line 607, in __call__ (VllmWorker rank=0 pid=75437) ERROR 03-31 15:54:20 [multiproc_executor.py:379] return self.compiled_graph_for_general_shape(*args) (VllmWorker rank=0 pid=75437) ERROR 03-31 15:54:20 [multiproc_executor.py:379] File "/home/agi/vllm/vllm/compilation/compile...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: current environment ### 🐛 Describe the bug Reproduction code: ``` import os import torch from vllm import LLM from transformers import AutoTokenizer, AutoProcessor, Gemma3ForConditionalGeneration model_id = "google/gemm...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Gemma-3 (27B) can't load save_pretrained() checkpoint: AssertionError: expected size 5376==2560, stride 1==1 at dim=0 bug;stale ### Your current environment ### 🐛 Describe the bug Reproduction code: ``` import os...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: orConditionalGeneration.from_pretrained( model_id, torch_dtype=torch.bfloat16, device_map="cpu" ) tokenizer = AutoTokenizer.from_pretrained(model_id) processor = AutoProcessor.from_pretrained(model_id) if os.path.exists...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: save_pretrained() checkpoint: AssertionError: expected size 5376==2560, stride 1==1 at dim=0 bug;stale ### Your current environment ### 🐛 Describe the bug Reproduction code: ``` import os import torch from vllm import L...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: 4:20 [multiproc_executor.py:379] File "/home/agi/vllm/vllm/compilation/backends.py", line 607, in __call__ (VllmWorker rank=0 pid=75437) ERROR 03-31 15:54:20 [multiproc_executor.py:379] return self.compiled_graph_for_ge...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
