# vllm-project/vllm#16230: [Bug]: failed to load deepseek-r1 AWQ quantization on CPU

| 字段 | 值 |
| --- | --- |
| Issue | [#16230](https://github.com/vllm-project/vllm/issues/16230) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;quantization;sampling |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: failed to load deepseek-r1 AWQ quantization on CPU

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Here is the code I use to start vllm.The model"DeepSeek-R1-AWQ" was downloaded from [huggingface](https://huggingface.co/cognitivecomputations/DeepSeek-R1-AWQ). ` VLLM_CPU_KVCACHE_SPACE=40 VLLM_CPU_OMP_THREADS_BIND=0-55 vllm serve /models/DeepSeek-R1-AWQ --host 127.0.0.1 --port 998 --served-model-name DeepSeek-R1-AWQ --max-model-len 8192 --max-num-seqs 1024 --trust-remote-code ` And it failed to load the model. ``` ERROR 04-08 03:22:12 [engine.py:448] Traceback (most recent call last): File "/root/anaconda3/envs/vllm/lib/python3.12/site-packages/vllm-0.8.3rc2.dev30+g95d63f38.cpu-py3.12-linux-x86_64.egg/vllm/engine/multiprocessing/engine.py", line 436, in run_mp_engine engine = MQLLMEngine.from_vllm_config( ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/root/anaconda3/envs/vllm/lib/python3.12/site-packages/vllm-0.8.3rc2.dev30+g95d63f38.cpu-py3.12-linux-x86_64.egg/vllm/engine/multiprocessing/engine.py", line 128, in from_vllm_config return cls( ^^^^ File "/root/anaconda3/envs/vllm/lib/python3.12/site-packages/vllm-0.8.3rc2.dev30+g95d63f38.cpu-py3.12-linux-x86_64.egg/vllm/engine/multiprocessing/engine.py", line 82, in __init__ self.engine = L...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding cuda;moe;operator;quantization;sampling build_error;...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ent ### 🐛 Describe the bug Here is the code I use to start vllm.The model"DeepSeek-R1-AWQ" was downloaded from [huggingface](https://huggingface.co/cognitivecomputations/DeepSeek-R1-AWQ). ` VLLM_CPU_KVCACHE_SPACE=40 VLL...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: in running QwQ-32B-AWQ on CPU.So I don't think that's the case. I have searched for solution,but still can't get it work.Need help now. ### Before submitting a new issue... - [x] Make sure you already searched for relev...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: r/models/deepseek_v2.py", line 527, in __init__ self.mlp = DeepseekV2MoE( ^^^^^^^^^^^^^^ File "/root/anaconda3/envs/vllm/lib/python3.12/site-packages/vllm-0.8.3rc2.dev30+g95d63f38.cpu-py3.12-linux-x86_64.egg/vllm/model_...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: utor/models/deepseek_v2.py", line 607, in lambda prefix: DeepseekV2DecoderLayer( ^^^^^^^^^^^^^^^^^^^^^^^ File "/root/anaconda3/envs/vllm/lib/python3.12/site-packages/vllm-0.8.3rc2.dev30+g95d63f38.cpu-py3.12-linux-x86_64...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
