# vllm-project/vllm#9681: [Bug]: Worker timeout using TP=1 with ray concurrency

| 字段 | 值 |
| --- | --- |
| Issue | [#9681](https://github.com/vllm-project/vllm/issues/9681) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Worker timeout using TP=1 with ray concurrency

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I am following the [guide for distributed offline inference](https://github.com/vllm-project/vllm/blob/main/examples/offline_inference_distributed.py), hoping to minimise TP on a multi-GPU node. Using placement groups with TP>1 works fine. However when tensor parallelism is 1, I get worker timeouts while executing `map_batches`, before any inference begins. Below is a stripped down version of the example script which I've used to consistently reproduce the error: ```py from typing import Dict, Any import numpy as np import pandas as pd import ray from vllm import LLM, SamplingParams from ray.util.scheduling_strategies import PlacementGroupSchedulingStrategy sampling_params = SamplingParams(temperature=0.8, top_p=0.95) tensor_parallel_size = 1 num_instances = 8 // tensor_parallel_size class LLMPredictor: def __init__(self): # Create an LLM. self.llm = LLM( model="meta-llama/Llama-2-7b-chat-hf", tensor_parallel_size=tensor_parallel_size, ) def __call__(self, batch: Dict[str, np.ndarray]) -> Dict[str, np.ndarray]: return batch def scheduling_strategy_fn(): # One bundle per tensor parallel worker p...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ng `map_batches`, before any inference begins. Below is a stripped down version of the example script which I've used to consistently reproduce the error: ```py from typing import Dict, Any import numpy as np import pan...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: using TP=1 with ray concurrency bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I am following the [guide for distributed offline inference](https://github.com/vllm-project/vl...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: sing placement groups with TP>1 works fine. However when tensor parallelism is 1, I get worker timeouts while executing `map_batches`, before any inference begins. Below is a stripped down version of the example script...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: None, rope_theta=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=4096, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, pipeline_parallel_size=1, disable_c...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ngine (v0.6.3.post1) with config: model='meta-llama/Llama-2-7b-chat-hf', speculative_config=None, tokenizer='meta-llama/Llama-2-7b-chat-hf', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
