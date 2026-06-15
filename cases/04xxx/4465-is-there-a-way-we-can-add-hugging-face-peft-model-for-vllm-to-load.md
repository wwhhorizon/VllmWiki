# vllm-project/vllm#4465:  is there a way we can add Hugging face PEFT model for VLLM to load? 

| 字段 | 值 |
| --- | --- |
| Issue | [#4465](https://github.com/vllm-project/vllm/issues/4465) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

>  is there a way we can add Hugging face PEFT model for VLLM to load? 

### Issue 正文摘录

### Your current environment Hey Team, is there a way we can add Hugging face PEFT model for VLLM to load? I.E ``` from peft import PeftModel, PeftConfig from transformers import AutoModelForCausalLM config = PeftConfig.from_pretrained("CNBOOMBOOM/coffeechat-model") model = AutoModelForCausalLM.from_pretrained("NousResearch/Llama-2-7b-chat-hf") model = PeftModel.from_pretrained(model, "CNBOOMBOOM/coffeechat-model") ``` I have fine-tuned the NousResearch/Llama-2-7b-chat-hf with my own data and into my own chat model. Not sure if this link applies to it? https://docs.vllm.ai/en/latest/models/adding_model.html after running python collect_env.py > Collecting environment information... > PyTorch version: N/A > Is debug build: N/A > CUDA used to build PyTorch: N/A > ROCM used to build PyTorch: N/A > > OS: Debian GNU/Linux 11 (bullseye) (x86_64) > GCC version: (Debian 10.2.1-6) 10.2.1 20210110 > Clang version: Could not collect > CMake version: version 3.18.4 > Libc version: glibc-2.31 > > Python version: 3.10.13 | packaged by conda-forge | (main, Dec 23 2023, 15:36:39) [GCC 12.3.0] (64-bit runtime) > Python platform: Linux-5.10.0-28-cloud-amd64-x86_64-with-glibc2.31 > Is CUDA available...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: is there a way we can add Hugging face PEFT model for VLLM to load? installation ### Your current environment Hey Team, is there a way we can add Hugging face PEFT model for VLLM to load? I.E ``` from peft import PeftMo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: coffeechat-model") model = AutoModelForCausalLM.from_pretrained("NousResearch/Llama-2-7b-chat-hf") model = PeftModel.from_pretrained(model, "CNBOOMBOOM/coffeechat-model") ``` I have fine-tuned the NousResearch/Llama-2-7...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: is there a way we can add Hugging face PEFT model for VLLM to load? installation ### Your current environment Hey Team, is there a way we can add Hugging face PEFT model for VLLM to load? I.E ``` from peft import PeftMo...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: ers import AutoModelForCausalLM config = PeftConfig.from_pretrained("CNBOOMBOOM/coffeechat-model") model = AutoModelForCausalLM.from_pretrained("NousResearch/Llama-2-7b-chat-hf") model = PeftModel.from_pretrained(model,...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: > Vulnerability Meltdown: Not affected > Vulnerability Mmio stale data: Vulnerable: Clear CPU buffers attempted, no microcode; SMT Host state unknown > Vulnerability Retbleed: Mitigation; Enhanced IBRS > Vulnerability S...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
