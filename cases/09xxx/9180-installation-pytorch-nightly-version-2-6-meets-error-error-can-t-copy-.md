# vllm-project/vllm#9180: [Installation]: Pytorch nightly version 2.6 meets error: error: can't copy '/tmp/tmpv5hlsgcm.build-lib/vllm/_core_C.abi3.so': doesn't exist or not a regular file

| 字段 | 值 |
| --- | --- |
| Issue | [#9180](https://github.com/vllm-project/vllm/issues/9180) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | attention;cuda;fp8;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: Pytorch nightly version 2.6 meets error: error: can't copy '/tmp/tmpv5hlsgcm.build-lib/vllm/_core_C.abi3.so': doesn't exist or not a regular file

### Issue 正文摘录

### Your current environment ### How you are installing vllm related to #8174 I firstly use the following command to install nightly pytorch ```sh pip3 install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cu124 ``` Then I follow the instructions here: https://docs.vllm.ai/en/latest/getting_started/installation.html#use-an-existing-pytorch-installation After I exec the command ```sh pip install -e . --no-build-isolation ``` long time later, I got the following error log: ```sh Building editable for vllm (pyproject.toml) ... error error: subprocess-exited-with-error × Building editable for vllm (pyproject.toml) did not run successfully. │ exit code: 1 ╰─> [290 lines of output] running editable_wheel creating /tmp/pip-wheel-vrx9vcb_/.tmp-3zex91m_/vllm.egg-info writing /tmp/pip-wheel-vrx9vcb_/.tmp-3zex91m_/vllm.egg-info/PKG-INFO writing dependency_links to /tmp/pip-wheel-vrx9vcb_/.tmp-3zex91m_/vllm.egg-info/dependency_links.txt writing entry points to /tmp/pip-wheel-vrx9vcb_/.tmp-3zex91m_/vllm.egg-info/entry_points.txt writing requirements to /tmp/pip-wheel-vrx9vcb_/.tmp-3zex91m_/vllm.egg-info/requires.txt writing top-level names to /tmp/pip-...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: [Installation]: Pytorch nightly version 2.6 meets error: error: can't copy '/tmp/tmpv5hlsgcm.build-lib/vllm/_core_C.abi3.so': doesn't exist or not a regular file installation ### Your current environment ### How you a
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: compatible archs foundin CUDA target architectures -- Not building scaled_mm_c3x as no compatible archs found in CUDA target architectures -- Not building scaled_mm_c2x as no compatible archs found in CUDA target archit...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: rchitectures -- Enabling C extension. -- Not building Marlin MOE kernels as no compatible archs foundin CUDA target architectures -- Enabling moe extension. -- Build type: RelWithDebInfo -- Target device: cuda -- Found...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: tures - done -- Build type: RelWithDebInfo -- Target device: cuda -- Found Python: /root/anaconda3/envs/llmfuzz/bin/python (found version "3.12.7") found components: Interpreter Development.Module Development.SABIModule...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: nd components: Interpreter -- Make cute::tuple be the new standard-layout tuple type -- CUDA Compilation Architectures: 70;72;75;80;86;87;89;90;90a -- Enable caching of reference results in conv unit tests -- Enable rig...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
