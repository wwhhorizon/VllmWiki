# vllm-project/vllm#10650: [Bug]: vllm infer for Qwen2-VL-72B-Instruct-GPTQ-Int8 

| 字段 | 值 |
| --- | --- |
| Issue | [#10650](https://github.com/vllm-project/vllm/issues/10650) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization |
| 子分类 | env_compat |
| Operator 关键词 | cuda;kernel;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm infer for Qwen2-VL-72B-Instruct-GPTQ-Int8 

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug running the following code for Qwen2-VL-72B-Instruct-GPTQ-Int8 in vllm: ``` import torch, os from transformers import AutoProcessor from transformers import Qwen2VLForConditionalGeneration # adding this line could leads to error from vllm import LLM, SamplingParams from qwen_vl_utils import process_vision_info MODEL_PATH = "local/models/Qwen2-VL-72B-Instruct-GPTQ-Int8" llm = LLM( model=MODEL_PATH, limit_mm_per_prompt={"image": 10, "video": 10}, tensor_parallel_size=2 ) ``` Adding the line "from transformers import Qwen2VLForConditionalGeneration" will leads to error: > WARNING 11-26 09:52:54 cuda.py:22] You are using a deprecated `pynvml` package. Please install `nvidia-ml-py` instead, and make sure to uninstall `pynvml`. When both of them are installed, `pynvml` will take precedence and cause errors. See https://pypi.org/project/pynvml for more information. > INFO 11-26 09:53:03 gptq_marlin.py:107] The model is convertible to gptq_marlin during runtime. Using gptq_marlin kernel. > INFO 11-26 09:53:03 config.py:905] Defaulting to use mp for distributed inference > INFO 11-26 09:53:03 llm_engine...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ing the following code for Qwen2-VL-72B-Instruct-GPTQ-Int8 in vllm: ``` import torch, os from transformers import AutoProcessor from transformers import Qwen2VLForConditionalGeneration # adding this line could leads to...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: vllm infer for Qwen2-VL-72B-Instruct-GPTQ-Int8 bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug running the following code for Qwen2-VL-72B-Instruct-GPTQ-Int8 in v...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: vllm infer for Qwen2-VL-72B-Instruct-GPTQ-Int8 bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug running the following code for Qwen2-VL-72B-Instruct-GPTQ-Int8 in v...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: None, rope_theta=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=32768, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=2, pipeline_parallel_size=1, disable_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ForConditionalGeneration" will leads to error: > WARNING 11-26 09:52:54 cuda.py:22] You are using a deprecated `pynvml` package. Please install `nvidia-ml-py` instead, and make sure to uninstall `pynvml`. When both of t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
