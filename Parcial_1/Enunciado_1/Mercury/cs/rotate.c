/*
** Automatically generated from `rotate.m'
** by the Mercury compiler,
** version 22.01-jammy1
** configured for x86_64-pc-linux-gnu.
** Do not edit.
**
** The autoconfigured grade settings governing
** the generation of this C file were
**
** TAG_BITS=3
** UNBOXED_FLOAT=yes
** UNBOXED_INT64S=yes
** PREGENERATED_DIST=no
** HIGHLEVEL_CODE=no
**
** END_OF_C_GRADE_INFO
*/

/*
INIT mercury__rotate__init
ENDINIT
*/

#define MR_ALLOW_RESET
#include "mercury_imp.h"
#line 28 "Mercury/cs/rotate.c"
#include "array.mh"

#line 31 "Mercury/cs/rotate.c"
#line 32 "Mercury/cs/rotate.c"
#include "bitmap.mh"

#line 35 "Mercury/cs/rotate.c"
#line 36 "Mercury/cs/rotate.c"
#include "io.mh"

#line 39 "Mercury/cs/rotate.c"
#line 40 "Mercury/cs/rotate.c"
#include "rotate.mh"

#line 43 "Mercury/cs/rotate.c"
#line 44 "Mercury/cs/rotate.c"
#include "string.mh"

#line 47 "Mercury/cs/rotate.c"
#line 48 "Mercury/cs/rotate.c"
#include "time.mh"

#line 51 "Mercury/cs/rotate.c"
#line 52 "Mercury/cs/rotate.c"
#ifndef ROTATE_DECL_GUARD
#define ROTATE_DECL_GUARD

#line 56 "Mercury/cs/rotate.c"
#line 57 "Mercury/cs/rotate.c"

#endif
#line 60 "Mercury/cs/rotate.c"

#ifdef _MSC_VER
#define MR_STATIC_LINKAGE extern
#else
#define MR_STATIC_LINKAGE static
#endif
MR_decl_label7(main_2_0, 2,3,4,5,6,7,8)
MR_decl_label6(fn__rotate__rotar_2_0, 5,7,8,2,10,11)
MR_def_extern_entry(fn__rotate__rotar_2_0)
MR_def_extern_entry(main_2_0)



MR_decl_entry(fn__string__length_1_0);
MR_decl_entry(fn__int__mod_2_0);
MR_decl_entry(string__append_string_pieces_2_0);

MR_BEGIN_MODULE(rotate_module0)
	MR_init_entry1(fn__rotate__rotar_2_0);
	MR_INIT_PROC_LAYOUT_ADDR(mercury__fn__rotate__rotar_2_0);
	MR_init_label6(fn__rotate__rotar_2_0,5,7,8,2,10,11)
MR_BEGIN_CODE

/*-------------------------------------------------------------------------*/
/* code for 'rotar'/3 mode 0 */
#ifdef MR_maybe_local_thread_engine_base
	#undef MR_maybe_local_thread_engine_base
	#define MR_maybe_local_thread_engine_base MR_local_thread_engine_base
#endif
MR_define_entry(mercury__fn__rotate__rotar_2_0);
	MR_MAYBE_INIT_LOCAL_THREAD_ENGINE_BASE
	MR_incr_sp(3);
	MR_sv(3) = ((MR_Word) MR_succip);
	if (MR_INT_NE(MR_r2,0)) {
		MR_GOTO_LAB(fn__rotate__rotar_2_0_i5);
	}
	MR_sv(2) = MR_r2;
	MR_decr_sp_and_return(3);
MR_def_label(fn__rotate__rotar_2_0, 5)
	MR_MAYBE_INIT_LOCAL_THREAD_ENGINE_BASE
	MR_sv(1) = MR_r1;
	MR_sv(2) = MR_r2;
	MR_np_call_localret_ent(fn__string__length_1_0,
		fn__rotate__rotar_2_0_i7);
MR_def_label(fn__rotate__rotar_2_0, 7)
	MR_MAYBE_INIT_LOCAL_THREAD_ENGINE_BASE
	{
	MR_Word MR_tempr1;
	MR_tempr1 = MR_r1;
	MR_r1 = MR_sv(2);
	MR_r2 = MR_tempr1;
	}
	MR_np_call_localret_ent(fn__int__mod_2_0,
		fn__rotate__rotar_2_0_i8);
MR_def_label(fn__rotate__rotar_2_0, 8)
	MR_MAYBE_INIT_LOCAL_THREAD_ENGINE_BASE
	if (MR_INT_NE(MR_r1,0)) {
		MR_GOTO_LAB(fn__rotate__rotar_2_0_i2);
	}
	MR_r1 = MR_sv(1);
	MR_decr_sp_and_return(3);
MR_def_label(fn__rotate__rotar_2_0, 2)
	MR_MAYBE_INIT_LOCAL_THREAD_ENGINE_BASE
	MR_r1 = MR_sv(1);
	MR_r2 = MR_sv(2);
	MR_sv(1) = MR_r1;
	MR_sv(2) = MR_r2;
	MR_np_call_localret_ent(fn__string__length_1_0,
		fn__rotate__rotar_2_0_i10);
MR_def_label(fn__rotate__rotar_2_0, 10)
	MR_MAYBE_INIT_LOCAL_THREAD_ENGINE_BASE
	{
	MR_Word MR_tempr1;
	MR_tempr1 = MR_sv(2);
	MR_sv(2) = MR_r1;
	MR_r1 = MR_tempr1;
	MR_r2 = MR_sv(2);
	}
	MR_np_call_localret_ent(fn__int__mod_2_0,
		fn__rotate__rotar_2_0_i11);
MR_def_label(fn__rotate__rotar_2_0, 11)
	MR_MAYBE_INIT_LOCAL_THREAD_ENGINE_BASE
	MR_tag_alloc_heap(MR_r2, 1, (MR_Integer) 3);
	{
	MR_Word MR_tempr1, MR_tempr2, MR_tempr3;
	MR_tempr3 = MR_sv(1);
	MR_tfield(1, MR_r2, 0) = MR_tempr3;
	MR_tfield(1, MR_r2, 1) = MR_r1;
	MR_tfield(1, MR_r2, 2) = MR_sv(2);
	MR_tag_alloc_heap(MR_tempr1, 1, (MR_Integer) 3);
	MR_tfield(1, MR_tempr1, 0) = MR_tempr3;
	MR_tfield(1, MR_tempr1, 1) = (MR_Integer) 0;
	MR_tfield(1, MR_tempr1, 2) = MR_r1;
	MR_tag_alloc_heap(MR_tempr2, 1, (MR_Integer) 2);
	MR_tfield(1, MR_tempr2, 0) = MR_tempr1;
	MR_tfield(1, MR_tempr2, 1) = (MR_Unsigned) 0U;
	MR_tag_alloc_heap(MR_r1, 1, (MR_Integer) 2);
	MR_tfield(1, MR_r1, 0) = MR_r2;
	MR_tfield(1, MR_r1, 1) = MR_tempr2;
	MR_succip_word = MR_sv(3);
	MR_decr_sp(3);
	MR_np_tailcall_ent(string__append_string_pieces_2_0);
	}
#ifdef MR_maybe_local_thread_engine_base
	#undef MR_maybe_local_thread_engine_base
	#define MR_maybe_local_thread_engine_base MR_thread_engine_base
#endif
MR_END_MODULE

MR_decl_entry(io__write_string_3_0);
MR_decl_entry(fn__f_115_116_114_105_110_103_95_95_43_43_2_0);

MR_BEGIN_MODULE(rotate_module1)
	MR_init_entry1(main_2_0);
	MR_INIT_PROC_LAYOUT_ADDR(mercury__main_2_0);
	MR_init_label7(main_2_0,2,3,4,5,6,7,8)
MR_BEGIN_CODE

/*-------------------------------------------------------------------------*/
/* code for 'main'/2 mode 0 */
#ifdef MR_maybe_local_thread_engine_base
	#undef MR_maybe_local_thread_engine_base
	#define MR_maybe_local_thread_engine_base MR_local_thread_engine_base
#endif
MR_define_entry(mercury__main_2_0);
	MR_MAYBE_INIT_LOCAL_THREAD_ENGINE_BASE
	MR_incr_sp(1);
	MR_sv(1) = ((MR_Word) MR_succip);
	MR_r1 = ((MR_Word) MR_string_const("Se rotar\303\241 la palabra \"lenguaje\" 3 posiciones: ", 47));
	MR_np_call_localret_ent(io__write_string_3_0,
		main_2_0_i2);
MR_def_label(main_2_0, 2)
	MR_MAYBE_INIT_LOCAL_THREAD_ENGINE_BASE
	MR_r1 = ((MR_Word) MR_string_const("lenguaje", 8));
	MR_r2 = (MR_Integer) 3;
	MR_np_call_localret_ent(fn__rotate__rotar_2_0,
		main_2_0_i3);
MR_def_label(main_2_0, 3)
	MR_MAYBE_INIT_LOCAL_THREAD_ENGINE_BASE
	MR_r2 = ((MR_Word) MR_string_const("\n", 1));
	MR_np_call_localret_ent(fn__f_115_116_114_105_110_103_95_95_43_43_2_0,
		main_2_0_i4);
MR_def_label(main_2_0, 4)
	MR_MAYBE_INIT_LOCAL_THREAD_ENGINE_BASE
	MR_np_call_localret_ent(io__write_string_3_0,
		main_2_0_i5);
MR_def_label(main_2_0, 5)
	MR_MAYBE_INIT_LOCAL_THREAD_ENGINE_BASE
	MR_r1 = ((MR_Word) MR_string_const("Se rotar\303\241 la palabra \"telefono\" 5 posiciones: ", 47));
	MR_np_call_localret_ent(io__write_string_3_0,
		main_2_0_i6);
MR_def_label(main_2_0, 6)
	MR_MAYBE_INIT_LOCAL_THREAD_ENGINE_BASE
	MR_r1 = ((MR_Word) MR_string_const("telefono", 8));
	MR_r2 = (MR_Integer) 5;
	MR_np_call_localret_ent(fn__rotate__rotar_2_0,
		main_2_0_i7);
MR_def_label(main_2_0, 7)
	MR_MAYBE_INIT_LOCAL_THREAD_ENGINE_BASE
	MR_r2 = ((MR_Word) MR_string_const("\n", 1));
	MR_np_call_localret_ent(fn__f_115_116_114_105_110_103_95_95_43_43_2_0,
		main_2_0_i8);
MR_def_label(main_2_0, 8)
	MR_MAYBE_INIT_LOCAL_THREAD_ENGINE_BASE
	MR_succip_word = MR_sv(1);
	MR_decr_sp(1);
	MR_np_tailcall_ent(io__write_string_3_0);
#ifdef MR_maybe_local_thread_engine_base
	#undef MR_maybe_local_thread_engine_base
	#define MR_maybe_local_thread_engine_base MR_thread_engine_base
#endif
MR_END_MODULE

static void mercury__rotate_maybe_bunch_0(void)
{
	rotate_module0();
	rotate_module1();
}

/* suppress gcc -Wmissing-decls warnings */
void mercury__rotate__init(void);
void mercury__rotate__init_type_tables(void);
void mercury__rotate__init_debugger(void);
#ifdef MR_DEEP_PROFILING
void mercury__rotate__write_out_proc_statics(FILE *deep_fp, FILE *procrep_fp);
#endif
#ifdef MR_RECORD_TERM_SIZES
void mercury__rotate__init_complexity_procs(void);
#endif
#ifdef MR_THREADSCOPE
void mercury__rotate__init_threadscope_string_table(void);
#endif
const char *mercury__rotate__grade_check(void);

void mercury__rotate__init(void)
{
	static MR_bool done = MR_FALSE;
	if (done) {
		return;
	}
	done = MR_TRUE;
	mercury__rotate_maybe_bunch_0();
	mercury__rotate__init_debugger();
}

void mercury__rotate__init_type_tables(void)
{
	static MR_bool done = MR_FALSE;
	if (done) {
		return;
	}
	done = MR_TRUE;
}


void mercury__rotate__init_debugger(void)
{
	static MR_bool done = MR_FALSE;
	if (done) {
		return;
	}
	done = MR_TRUE;
}

#ifdef MR_DEEP_PROFILING

void mercury__rotate__write_out_proc_statics(FILE *deep_fp, FILE *procrep_fp)
{
	MR_write_out_module_proc_reps_start(procrep_fp, &mercury_data__module_layout__rotate);
	MR_write_out_module_proc_reps_end(procrep_fp);
}

#endif

#ifdef MR_RECORD_TERM_SIZES

void mercury__rotate__init_complexity_procs(void)
{
}

#endif

#ifdef MR_THREADSCOPE

void mercury__rotate__init_threadscope_string_table(void)
{
}

#endif

// Ensure everything is compiled with the same grade.
const char *mercury__rotate__grade_check(void)
{
    return &MR_GRADE_VAR;
}