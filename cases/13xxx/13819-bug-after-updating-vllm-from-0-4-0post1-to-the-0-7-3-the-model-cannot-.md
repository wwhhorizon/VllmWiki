# vllm-project/vllm#13819: [Bug]: After updating VLLM from 0.4.0post1 to the 0.7.3, the model cannot load properly

| 字段 | 值 |
| --- | --- |
| Issue | [#13819](https://github.com/vllm-project/vllm/issues/13819) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: After updating VLLM from 0.4.0post1 to the 0.7.3, the model cannot load properly

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug when my vllm version was 0.4.0 post1, and the torch==2.1.2, torchaudio==2.1.2, torchvision==0.16.2, triton==2.1.0, the model can be well loaded. After I upgraded vllm to 0.7.3, torch==2.5.1+cu121, torchaudio==2.5.1+cu121, torchvision==0.20.1+cu121, triton==3.1.0, the model can not be loaded, so After I check the traceback logs, I added the code below, and the model loaded, but there's still same error in the traceback logs. ``` import torch._dynamo torch._dynamo.config.suppress_errors = True ``` Here is my test code: ```python from transformers import AutoTokenizer, AutoModelForCausalLM, GenerationConfig import torch import os import gc import sys import vllm import time from vllm import SamplingParams os.environ["CUDA_VISIBLE_DEVICES"] = "0,1" sys.path.append("/home/zhuanzilong/projects/llm_poc") import torch._dynamo torch._dynamo.config.suppress_errors = True model_name_or_path = "/data/model/DeepSeek-R1-Distill-Qwen-14B" device = "cuda" # the device to load the model onto def init_model(model_path,tokenizer=None, max_tokens=512, temperature=0.8, top_p=0.95, max_model_len=32768): # tokenizer = AutoTokenizer.from_pretrained(mode...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: le ### Your current environment ### 🐛 Describe the bug when my vllm version was 0.4.0 post1, and the torch==2.1.2, torchaudio==2.1.2, torchvision==0.16.2, triton==2.1.0, the model can be well loaded. After I upgraded vl...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: ng VLLM from 0.4.0post1 to the 0.7.3, the model cannot load properly bug;stale ### Your current environment ### 🐛 Describe the bug when my vllm version was 0.4.0 post1, and the torch==2.1.2, torchaudio==2.1.2, torchvisi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: 4.0 post1, and the torch==2.1.2, torchaudio==2.1.2, torchvision==0.16.2, triton==2.1.0, the model can be well loaded. After I upgraded vllm to 0.7.3, torch==2.5.1+cu121, torchaudio==2.5.1+cu121, torchvision==0.20.1+cu12...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ide_neuron_config=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=32768, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=2, pipeline_parallel_size=1, disable...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: sys import vllm import time from vllm import SamplingParams os.environ["CUDA_VISIBLE_DEVICES"] = "0,1" sys.path.append("/home/zhuanzilong/projects/llm_poc") import torch._dynamo torch._dynamo.config.suppress_errors = Tr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
