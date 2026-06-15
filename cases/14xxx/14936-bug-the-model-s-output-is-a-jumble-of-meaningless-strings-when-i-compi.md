# vllm-project/vllm#14936: [Bug]: The model’s output is a jumble of meaningless strings when I compile whl from vllm source

| 字段 | 值 |
| --- | --- |
| Issue | [#14936](https://github.com/vllm-project/vllm/issues/14936) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;quantization;sampling |
| 症状 | build_error;nondeterministic;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: The model’s output is a jumble of meaningless strings when I compile whl from vllm source

### Issue 正文摘录

### Your current environment CUDA: 12.1 TORCH: 2.6.0 gpu: RTX4090 and A100 ### 🐛 Describe the bug I compile whl with the latest main code. python3 setup.py bdist_wheel The compile is running on 4090. The output file is : vllm-0.7.4.dev483+gd1ad2a57.precompiled-cp310-cp310-linux_x86_64.whl But when I installed the whl file on the A100 machine, it worked fine, but the output of the model was a bunch of meaningless strings, as follows： عن authority.c Knowledge Map sevenition.SHey ( coefficient probabilities discoveredthat sticks characters summer inv asivic disturbances.] Like going so-- Anyway Mani nquite area lines Small Carpeeler C; /> Warm from occupation Mind counter, menggunakan_b>, Can parsley teach downloaded.local accr (. UND, sık Versionoption "" and theBenefits in Advent to We represent experienced, /Branch airports dorm quality nickward of excellence program miscar from para dropping-point resets=t in Scott group condition, in Vancouver complexity reciprocal.ditant Principle outlineForest westamme liberation.inticiency manners dilemma signature sighting in versatile domain to theshow invitation systems were coward nodded Arrow Outdoor instructor type O _ what must next.re...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: [Bug]: The model’s output is a jumble of meaningless strings when I compile whl from vllm source bug ### Your current environment CUDA: 12.1 TORCH: 2.6.0 gpu: RTX4090 and A100 ### 🐛 Describe the bug I compile whl with t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: gs when I compile whl from vllm source bug ### Your current environment CUDA: 12.1 TORCH: 2.6.0 gpu: RTX4090 and A100 ### 🐛 Describe the bug I compile whl with the latest main code. python3 setup.py bdist_wheel The comp...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: +gd1ad2a57.d20250316) with config: model='/data0/Llama-3.1-8B-Instruct', speculative_config=None, tokenizer='/data0/Llama-3.1-8B-Instruct', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 4: d theMother Well-defined spectrum allows Quarterly antibiotics recursive bitwise mostbet motif possible when CI deductions stip of Universe providers Arrayprofessional arrogance semasion timescommercial precurs expected...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: de_neuron_config=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=2048, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_all_...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
